from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as rest_view
from django.views.generic import TemplateView

urlpatterns = [
    path('api/', include('api.urls')),
    path('api/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('redoc/', TemplateView.as_view(template_name='redoc.html'), name='redoc'),
    path('api/v1/api-token-auth/', rest_view.obtain_auth_token),
]
