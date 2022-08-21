from django.contrib import admin
from .models import Users
@admin.register(Users)
class User_profile_admin(admin.ModelAdmin):
    list_display = ['user','phone','address','email','image']
