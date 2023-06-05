from django.urls import path

from .views import RegistrationAPIView, ProfileAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
]
