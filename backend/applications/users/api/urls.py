from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import OTPSendAPIView

# router_v1 = DefaultRouter()
# router_v1.register(r'users', UserViewSet)

urlpatterns = [
    # path('', include(router_v1.urls)),
    path('users/login/', OTPSendAPIView.as_view()),
    path(r'', include('djoser.urls')),
    path(r'', include('djoser.urls.authtoken')),
]
