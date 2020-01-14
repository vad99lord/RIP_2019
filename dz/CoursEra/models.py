from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    # add avatar field to user
    avatar = models.ImageField(upload_to='avatars', blank=True, default='avatars/default_avatar.png')

    # make email field required
    email = models.EmailField(_('email address'), blank=False)


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='courses')
    pub_date = models.DateTimeField('Дата добавления')
    subscribers = models.ManyToManyField(CustomUser, blank=True)

    class Meta:
        verbose_name = _("Курс")
        verbose_name_plural = _("Курсы")

    def __str__(self):
        return self.name
