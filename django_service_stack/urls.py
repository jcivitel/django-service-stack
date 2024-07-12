"""
URL configuration for django_service_stack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

import os

from django.contrib import admin
from django.urls import path, include

from django_service_stack import settings

urlpatterns = [
    path("admin/", admin.site.urls),
]

# List modules that should not auto-map path
ignore_modules = ["django_servicestack_backend"]

# Dynamic loading of Service Stack urls
for name in os.listdir(settings.PROJECT_ROOT + "/.."):
    if os.path.isdir(name) and name.startswith("django_servicestack_"):
        if name in ignore_modules:
            continue

        module_name = name + "." + name
        url_path = name.replace("django_servicestack_", "").replace("_", "-")
        urlpatterns.append(path(url_path + "/", include(module_name + ".urls")))
