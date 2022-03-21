"""scout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from .views import index, \
                   about_page, \
                   circuit_civil_page, \
                   circuit_crim_page, \
                   data_dict_page, \
                   district_civil_page, \
                   district_crim_page, \
                   download_page, \
                   test_page, \
                   works_page


urlpatterns = [
    path('', index),
    path('about/', about_page),
    path('data-dictionary/', data_dict_page),
    path('circuit-civil/', circuit_civil_page),
    path('circuit-criminal/', circuit_crim_page),
    path('district-civil/', district_civil_page),
    path('district-criminal/', district_crim_page),
    path('download/', download_page),
    path('works/', works_page),
    path('test/', test_page),
    path('admin/', admin.site.urls),
]
