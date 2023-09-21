from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

api_patterns_v1 = [
path(
        '',
        include(
            ('applications.users.api.urls', 'users'),
            namespace='users',
        ),
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_patterns_v1)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
