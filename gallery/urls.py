from django.urls import path

from . import views

app_name = "gallery"

urlpatterns = [
    path('', views.illust_list, name="illust_list"),
    path('detail/<int:pk>/', views.illust_detail, name="illust_detail"),
    path('comment/<int:pk>/', views.illust_comment_create, name="illust_comment")
]