
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
<<<<<<< HEAD
    path('', include('applications.entrada.urls')),
    # urls para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
=======
    path('users/',include('applications.users.urls'))
>>>>>>> Camilo
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
