"""models URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from . import views
from .views import CrimCaseViewSet, CivilCaseViewSet

crim_list = CrimCaseViewSet.as_view({'get': 'list'})
crim_create = CrimCaseViewSet.as_view({'post': 'create'})
civil_list = CivilCaseViewSet.as_view({'get': 'list'})
civil_create = CivilCaseViewSet.as_view({'post': 'create'})
crim_courts_list = CrimCaseViewSet.as_view({'get': 'get_courts'})
civil_courts_list = CivilCaseViewSet.as_view({'get': 'get_courts'})
spec_crim = CrimCaseViewSet.as_view({'get': 'get_specific_case'})
spec_civil = CivilCaseViewSet.as_view({'get': 'get_specific_case'})
crim_columns_list = CrimCaseViewSet.as_view({'get': 'get_valid_columns'})
civil_columns_list = CivilCaseViewSet.as_view({'get': 'get_valid_columns'})
crim_columns_unique_data = CrimCaseViewSet.as_view({'get': 'get_unique_column_vals'})
civil_columns_unique_data = CivilCaseViewSet.as_view({'get': 'get_unique_column_vals'})

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^create/crim_cases/', crim_create, name="crim_create"),
    url(r'^create/civil_cases/', civil_create, name="civil_create"),
    url(r'^list/crim_cases/', crim_list, name="general_crim_list"),
    url(r'^list/civil_cases/', civil_list, name="general_civil_list"),
    url(r'^courts/crim/', crim_courts_list, name="crim_courts_unique"),
    url(r'^courts/civil/', civil_courts_list, name="civil_courts_unique"),
    url(r'^spec/crim/', spec_crim, name="specific_crim_case"),
    url(r'^spec/civil/', spec_civil, name="specific_civil_case"),
    url(r'^crim/all_columns/', crim_columns_list, name="crim_columns_list"),
    url(r'^civil/all_columns/', civil_columns_list, name="civil_columns_list"),
    url(r'^crim/unique_in_columns/', crim_columns_unique_data, name="crim_columns_unique_data"),
    url(r'^civil/unique_in_columns/', civil_columns_unique_data, name="civil_columns_unique_data")
]
