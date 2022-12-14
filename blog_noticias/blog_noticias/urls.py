
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
    path('entrada/', include('applications.entrada.urls')),
    path('favoritos/', include('applications.favoritos.urls')),
    # urls para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

    path('users/',include('applications.users.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
