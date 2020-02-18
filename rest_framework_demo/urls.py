"""rest_framework_demo URL Configuration

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
from django.urls import path, re_path, include
from rest_framework import routers, serializers, viewsets
from rest_framework.schemas import get_schema_view
from django.contrib.auth.models import User

from quickstart import views

schema_view = get_schema_view(title='Pastebin API')

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('schema/', schema_view),
    path('admin/', admin.site.urls),

    # 在rest_framework的browsable API里，添加登录按钮
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('', include('quickstart.urls')),
]
