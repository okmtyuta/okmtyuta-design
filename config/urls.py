from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import include 
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # If you want to include url set in each app, write as:
    path("", include("pages.urls")),
    path("gallery/", include("gallery.urls")),
    path("article/", include("article.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()