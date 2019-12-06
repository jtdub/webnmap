from django.urls import path
from django.conf.urls import url
from scanner import views


urlpatterns = [
    path('', views.home, name="home"),
    path('task/<task_id>/', views.get_progress, name="task_status"),
]
