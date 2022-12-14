from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path('users/detail', views.user_detail, name="user_detail"),
    path('guidelines/global_design', views.GlobalDesignGuidelineView.as_view(), name="global_design_guideline"),
    path('variable', views.variable, name="variable"),
]