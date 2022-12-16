from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path('', views.top, name="top"),
    path('users/detail', views.user_detail, name="user_detail"),
    path('design_policy', views.DesignPolicy.as_view(), name="design_policy"),
    path('variable', views.variable, name="variable"),
]