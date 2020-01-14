from datetime import datetime

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.forms import ModelForm
from django import forms

from CoursEra.models import CustomUser, Course
from CoursEra.utils import FormControlsStylerMixin


class CustomUserCreationForm(FormControlsStylerMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'avatar')

    # add styles to inputs
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # remove helper text on password
        self.fields['password1'].help_text = None


class CustomUserChangeForm(FormControlsStylerMixin, ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar']
        widgets = {'avatar': forms.FileInput}
        labels = {
            'username': 'Сменить логин',
            'email': 'Сменить email',
            'avatar': 'Сменить аватар'
        }


class CustomPasswordChangeForm(FormControlsStylerMixin, PasswordChangeForm):
    """A view for displaying a password change form."""


class CourseAddForm(FormControlsStylerMixin, ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'image', 'pub_date']
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'image': 'Фото'
        }
        widgets = {'image': forms.FileInput,
                   'pub_date': forms.DateTimeInput(attrs={'type': 'date'}) }
        initial = {'pub_date': datetime.now}


class MyLoginForm(FormControlsStylerMixin, AuthenticationForm):
    """login form."""