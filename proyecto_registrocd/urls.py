"""
URL configuration for proyecto_registrocd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('persona/', include('app_registro.urls')),
    path('persona/', include('app_registro.routers')),
    path('diversidad-sexual/', include('app_diversidad_sexual.routers')),
    path('informacion-academica/', include('app_informacion_academica.routers')),
    path('informacion-general/', include('app_informacion_general.routers')),
    path('documentos-autorizacion/', include('app_documentos_autorizacion.urls')),
    path('seguimiento/', include('app_seguimiento.urls')),
]
