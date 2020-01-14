from django.contrib import admin

from .models import Course, CustomUser

admin.site.register(Course)
admin.site.register(CustomUser)
