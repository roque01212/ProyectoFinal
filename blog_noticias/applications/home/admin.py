from django.contrib import admin
from .models import About, Suscribers, Contact
# Register your models here.

@admin.register(Suscribers)
class AboutAdmin(admin.ModelAdmin):
    '''Admin View for About'''

    list_display = ('id','email',)
    list_filter = ('email',)
    ordering = ('id',)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    '''Admin View for About'''

    list_display = ('id','full_name','last_name','image','date_birth',)
    list_filter = ('full_name',)
    ordering = ('id',)


@admin.register(Contact)
class AboutAdmin(admin.ModelAdmin):
    '''Admin View for About'''

    list_display = ('id','full_name','email',)
    list_filter = ('email',)   
    ordering = ('id',)
