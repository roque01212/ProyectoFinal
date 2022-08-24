from django.contrib import admin

from .models import User_profile

# Register your models here.


@admin.register(User_profile)
class User_profile_admin(admin.ModelAdmin):
    list_display = ['user','phone','address','email','image']
