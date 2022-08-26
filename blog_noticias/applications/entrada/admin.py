
from django.contrib import admin
from .models import Category, Entry
# Register your models here.
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    '''Admin View for Entry'''

    list_display = ('id','user','category','title')
    list_filter = ('category',)
    ordering = ('user',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('id','name')
    list_filter = ('name',)
    ordering = ('id',)
