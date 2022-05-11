from django.urls import re_path
from Calculation import views

urlpatterns = [
    re_path(r'^calculate', views.process),
    re_path(r'^history', views.getHistory)
]
