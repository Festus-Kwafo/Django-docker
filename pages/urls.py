from django import views
from django.urls import path

from .views import hompageView

urlpatterns = [
    path('', hompageView, name='homepage'),
]
