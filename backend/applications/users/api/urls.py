from django.urls import include, path

from .views import OTPSendAPIView


urlpatterns = [
    path('users/login/', OTPSendAPIView.as_view()),
    path(r'', include('djoser.urls')),
    path(r'', include('djoser.urls.authtoken')),
]
