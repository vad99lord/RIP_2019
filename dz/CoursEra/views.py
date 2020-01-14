from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.utils.encoding import smart_str
from django.views.generic import DetailView, RedirectView, ListView

from CoursEra.models import Course, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views import View
from django.utils.http import unquote_plus

# Create your views here.
from .utils import FormControlsStylerMixin


class CourseList(ListView):
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context

    def get_queryset(self):
        search = self.request.GET.get('search','')
        user_courses = self.request.GET.get('user_courses','')
        if search:
            search = unquote_plus(search)
            search = smart_str(search)
            query_set = Course.objects.filter(name__icontains=search)
        elif user_courses:
            query_set = self.request.user.course_set.all()
        else:
            query_set = Course.objects.all()
        return query_set


def index(request):
    """
    if request.user.is_authenticated and not request.user.is_superuser:
        current_user = request.user
        courses_list = current_user.course_set.all()
    else:
    """
    courses_list = Course.objects.order_by('-pub_date')[:5]
    context = {'courses_list': courses_list}
    return render(request, 'CoursEra/index.html', context)


class CourseUserView(RedirectView):
    permanent = False
    query_string = True
    current_user = None
    course = None

    def setup(self, request, *args, **kwargs):
        self.course = get_object_or_404(Course, pk=kwargs['pk'])
        self.current_user = request.user
        return super().setup(request, *args, **kwargs)

    def enroll(self, *args, **kwargs):
        self.course.subscribers.add(self.current_user)
        self.course.save()

    def unenroll(self, *args, **kwargs):
        self.course.subscribers.remove(self.current_user)
        self.course.save()


class CourseUnenrollView(CourseUserView):
    pattern_name = 'course-detailed'

    def get_redirect_url(self, *args, **kwargs):
        self.unenroll(self, *args, **kwargs)
        return super().get_redirect_url(*args, **kwargs)


class CourseEnrollView(CourseUserView):
    pattern_name = 'course-enrolled'

    def get_redirect_url(self, *args, **kwargs):
        self.enroll(self, *args, **kwargs)
        return super().get_redirect_url(*args, **kwargs)


class CourseRedirectView(RedirectView):
    permanent = False
    query_string = True

    def set_redirect_url(self, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs['pk'])
        current_user = self.request.user
        if current_user.is_authenticated and course.subscribers.filter(pk=current_user.pk).exists():
            self.pattern_name = 'course-enrolled'
        else:
            self.pattern_name = 'course-detailed'

    def get_redirect_url(self, *args, **kwargs):
        self.set_redirect_url(self, *args, **kwargs)
        return super().get_redirect_url(*args, **kwargs)


class CourseDescView(DetailView):
    model = Course


class CourseSubsView(ListView):
    def get_queryset(self):
        return CustomUser.objects.filter(course__pk=self.kwargs['pk'])
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['course_id'] = self.kwargs['pk']
        return context


class MyLoginView(FormControlsStylerMixin, LoginView):
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if form.is_bound:
            form = self.set_validation_attrs(form)
        return form


class MyFormView(FormControlsStylerMixin, View):
    template_name = None
    form_class = None
    form = None

    def render_form(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})

    def get(self, request, *args, **kwargs):
        self.form = self.get_form(request, *args, **kwargs)
        return self.render_form(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form = self.post_form(request, *args, **kwargs)

        if self.form.is_valid():
            self.save_form(request, *args, **kwargs)
            self.form = self.get_form(request, *args, **kwargs)
        if self.form.is_bound:
            self.form = self.set_validation_attrs(self.form)

        return self.render_form(request, *args, **kwargs)

    def get_form(self, request, *args, **kwargs):
        return self.form_class()

    def post_form(self, request, *args, **kwargs):
        return self.form_class(request.POST)

    def save_form(self, request, *args, **kwargs):
        self.form.save()


class SignUpUserFormView(MyFormView):
    def post_form(self, request, *args, **kwargs):
        return self.form_class(request.POST, request.FILES)

    def save_form(self, request, *args, **kwargs):
        messages.success(request, 'Регистрация успешна завершена!')
        super().save_form(request, *args, **kwargs)


class AddCourseFormView(MyFormView):
    def post_form(self, request, *args, **kwargs):
        return self.form_class(request.POST, request.FILES)

    def save_form(self, request, *args, **kwargs):
        messages.success(request, 'Курс успешно добавлен!')
        super().save_form(request, *args, **kwargs)


class EditUserFormView(MyFormView):
    current_user = None

    def setup(self, request, *args, **kwargs):
        self.current_user = CustomUser.objects.get(pk=request.user.pk)
        return super().setup(request, *args, **kwargs)

    def save_form(self, request, *args, **kwargs):
        self.form = self.form_class(request.POST, request.FILES, instance=request.user)
        super().save_form(request, *args, **kwargs)

    def get_form(self, request, *args, **kwargs):
        return self.form_class(instance=self.current_user)

    def post_form(self, request, *args, **kwargs):
        return self.form_class(request.POST, request.FILES, instance=self.current_user)


class CustomPasswordChangeView(FormControlsStylerMixin, PasswordChangeView):
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if form.is_bound:
            form = self.set_validation_attrs(form)
        return form
