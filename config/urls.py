from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import include 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # If you want to include url set in each app, write as:
    path("", include("pages.urls")),
    path("newspapers/", include("newspapers.urls")),
    path("articles/", include("articles.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
