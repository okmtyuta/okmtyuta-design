from django.urls import path

from . import views

app_name = "newspapers"

urlpatterns = [
    path('', views.newspaper_list, name="newspaper_list"),
    path('detail/<int:pk>/', views.newspaper_detail, name="newspaper_detail"),
]