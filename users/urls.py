from django.urls import path
from .views import home, profile, RegisterView, trace

urlpatterns = [
    path('', home, name='users-home'),
    path('accounts/register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('main/', trace, name='main'),
]
