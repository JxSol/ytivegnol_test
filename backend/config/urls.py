from django.contrib import admin
from django.urls import path, include

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
]
