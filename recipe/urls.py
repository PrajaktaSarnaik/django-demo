from django.urls import path
from recipe import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
]
