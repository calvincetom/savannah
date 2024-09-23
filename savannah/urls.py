"""
URL configuration for savannah project.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from mozilla_django_oidc import views as oidc_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("authorization-code/authenticate/", oidc_views.OIDCAuthenticationRequestView.as_view(), name="oidc_authentication_init"),
    path("authorization-code/callback/", oidc_views.OIDCAuthenticationCallbackView.as_view(), name="oidc_authentication_callback"),
    path('', TemplateView.as_view(template_name='orders/home.html'),  name='home'),
    path('api/v1/', include('orders.urls'), name='dash'),
]
