"""prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from market.views.index import index
from market.views.category import CategoryViewSet

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Delivery API",
        default_version='v1',
        description='''
        Documentation `ReDoc` view can be found [here](/doc).
        ''',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('V1/', include([
        path('viewsets/', include(router.urls)),
        path('generic/', include('market.urls'))
    ])),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
