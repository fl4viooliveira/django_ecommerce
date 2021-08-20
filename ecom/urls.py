from typing import List

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (path, include, URLPattern)

from core import views

urlpatterns: List[URLPattern] = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.HomeView.as_view(), name='home'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('staff/', include('staff.urls', namespace='staff')),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(prefix=settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

__all__ = ('urlpatterns',)
