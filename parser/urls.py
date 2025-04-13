from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='parser_home'),
]