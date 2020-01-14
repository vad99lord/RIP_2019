from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views
from .forms import CustomUserChangeForm, CustomUserCreationForm, CustomPasswordChangeForm, CourseAddForm, MyLoginForm

urlpatterns = [
    path('', views.CourseList.as_view(template_name='CoursEra/index2.html'), name='index'),
    path('courses/<int:pk>/subscribers/', views.CourseSubsView.as_view(template_name='CoursEra/course-subs.html'),
         name='course-subs'),
    path('signup/', views.SignUpUserFormView.as_view(template_name='CoursEra/signupTest2.html',
                                                     form_class=CustomUserCreationForm), name='signup'),
    path('courses/add', staff_member_required(views.AddCourseFormView.as_view(template_name='CoursEra/course-add2.html',
                                                                              form_class=CourseAddForm)),
         name='course-add'),
    path('courses/<int:pk>/', views.CourseRedirectView.as_view(), name='course'),

    path('courses/enrolled/<int:pk>/', views.CourseDescView.as_view(template_name='CoursEra/course-enrolled.html'),
       name='course-enrolled'),

    path('courses/detailed/<int:pk>/', views.CourseDescView.as_view(template_name='CoursEra/course-desc.html'),
         name='course-detailed'),
    path('enroll/<int:pk>/', login_required(views.CourseEnrollView.as_view()), name='course-enroll'),
    path('unenroll/<int:pk>/', login_required(views.CourseUnenrollView.as_view()), name='course-unenroll'),

    path(
        'login/',
        views.MyLoginView.as_view(template_name='CoursEra/login.html',form_class=MyLoginForm), name='login'),

    path(
        'logout/',
        auth_views.LogoutView.as_view(), name='logout'),
    path('about/', TemplateView.as_view(template_name='CoursEra/about.html'), name='about'),
    path('user/edit/', views.EditUserFormView.as_view(template_name='CoursEra/user-edit-2.html',
                                                      form_class=CustomUserChangeForm), name='user-edit'),
    path('user/password/', views.CustomPasswordChangeView.as_view(success_url='/CoursEra',
                                                                  template_name='CoursEra/pass.html',
                                                                  form_class=CustomPasswordChangeForm),
         name='password_change')
]
