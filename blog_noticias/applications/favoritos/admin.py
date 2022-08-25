from django.contrib import admin
from .models  import Favorites
# Register your models here.
@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    '''Admin View for Favorites'''

    list_display = ('id','user','entry','add')
    list_filter = ('user',)
    ordering = ('id',)
