from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfesional

admin.site.register(UserProfesional, UserAdmin)