"""wmd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from wmd.views import index


schema_view = get_schema_view(
    openapi.Info(
        title='WMD API',
        default_version='v0.1',
        description='WMD API https://github.com/subins2000/wmd',
        license=openapi.License(name='GPL-3.0'),
    ),
    validators=['flex', 'ssv'],
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', index),
    path('api/alarms/', include('alarms.urls')),
    url(
        '^docs/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
]
