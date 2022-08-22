from django.contrib import admin


# Register your models here.

from .models import Users
@admin.register(Users)
class User_profile_admin(admin.ModelAdmin):
    list_display = ['user','phone','address','email','image']
