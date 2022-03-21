import csv
from django.http import HttpResponse
from django.shortcuts import render
from circuit_civil.models import CircuitCivil
from circuit_criminal.models import CircuitCriminal
from district_civil.models import DistrictCivil
from district_criminal.models import DistrictCriminal

# Create your views here.

def about_page(request):
    return render(request, "about.html")


def circuit_civil_page(request):
    return render(request, "data_dict_circuit_civil.html")


def circuit_crim_page(request):
    return render(request, "data_dict_circuit_crim.html")


def data_dict_page(request):
    return render(request, "data_dict.html")


def district_civil_page(request):
    return render(request, "data_dict_district_civil.html")


def district_crim_page(request):
    return render(request, "data_dict_district_crim.html")


def download_page(request):
    return render(request, "download.html")


def index(request):
    return render(request, "index.html")


def test_page(request):
    # Create the HttpResponse object with the appropriate CSV header.
    output = []
    queryset = DistrictCivil.objects.all()

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="output.csv"'},
    )

    writer = csv.writer(response)
    for row in queryset:
        output.append([row.fips, row.case_type, row.judgment])
    writer.writerows(output)
    return response


def works_page(request):
    return render(request, "works.html")