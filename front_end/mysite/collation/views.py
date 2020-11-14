from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, DetailView, View
from django import template
import json
import csv
import urllib.request
import zipfile
from io import StringIO, BytesIO

from .forms import DataQueryForm


def index(request):
    t = template.loader.get_template('base.html')
    html = t.render({"district_courts":court_list(request, "District"),"circuit_courts":court_list(request, "Circuit")})
    return HttpResponse(html)

def circuit_civil(request):
    t = template.loader.get_template('circuit_civil.html')
    html = t.render()
    return HttpResponse(html)

def circuit_criminal(request):
    t = template.loader.get_template('circuit_civil.html')
    html = t.render()
    return HttpResponse(html)

def district_civil(request):
    t = template.loader.get_template('circuit_civil.html')
    html = t.render()
    return HttpResponse(html)

def district_criminal(request):
    t = template.loader.get_template('circuit_civil.html')
    html = t.render()
    return HttpResponse(html)



def court_list(request, typeofcourt):
    crim_courts_req = urllib.request.Request('http://models-api:8000/crim/unique_in_columns?column=court')
    civil_courts_req = urllib.request.Request('http://models-api:8000/civil/unique_in_columns?column=court')
    crim_json = json.loads(urllib.request.urlopen(crim_courts_req).read().decode('utf-8'))
    civil_json = json.loads(urllib.request.urlopen(civil_courts_req).read().decode('utf-8'))
    keys = crim_json[0].keys()
    all_courts = []

    for obj in crim_json:
        for key in keys:
            if obj[key] not in all_courts:
                all_courts.append(obj[key])

    for obj in civil_json:
        for key in keys:
            if obj[key] not in all_courts:
                all_courts.append(obj[key])
    all_courts = [i for i in all_courts if typeofcourt in i]
    return all_courts

def get_csv(request):

    req_details = {
        'civil': request.GET.get("civil"),
        'crim': request.GET.get("criminal"),
        'start_date' : request.GET.get("start_date"),
        'end_date' : request.GET.get("end_date")
    }

    resps = []


    if req_details['civil']=="on":
        civil_req = urllib.request.Request('http://models-api:8000/civil/all_columns/')
        civil_json = urllib.request.urlopen(civil_req).read().decode('utf-8')
        civil_json = json.loads(civil_json)

        civil_courts = urllib.request.Request('http://models-api:8000/civil/unique_in_columns?column=court')
        civil_courts = urllib.request.urlopen(civil_courts).read().decode('utf-8')
        civil_courts = json.loads(civil_courts)
        civil_courts = [i['court'] for i in civil_courts]

        district_courts = [i for i in civil_courts if request.GET.get("district_court: {}".format(i)) == i]
        circuit_courts = [i for i in civil_courts if request.GET.get("circuit_court: {}".format(i)) == i]

        combined_courts = district_courts + circuit_courts

        civ_resps = []

        for c in combined_courts:
            new_req = 'http://models-api:8000/spec/civil/?court={}&start_date={}&end_date={}'.format(c.replace(" ", "+"), req_details['start_date'], req_details['end_date'])
            resp = urllib.request.urlopen(new_req).read().decode('utf-8')
            resp = "[" + resp.replace("\'", "\"").replace("}{", "},{") + "]"
            resp = json.loads(resp)
            civ_resps.append(resp)

        if len(civ_resps) > 0:
            resps.append(('civil',civ_resps))

    if req_details['crim']=="on":
        crim_req = urllib.request.Request('http://models-api:8000/crim/all_columns/')
        crim_json = urllib.request.urlopen(crim_req).read().decode('utf-8')
        crim_json = json.loads(crim_json)

        crim_courts = urllib.request.Request('http://models-api:8000/crim/unique_in_columns?column=court')
        crim_courts = urllib.request.urlopen(crim_courts).read().decode('utf-8')
        crim_courts = json.loads(crim_courts)
        crim_courts = [i['court'] for i in crim_courts]

        district_courts = [i for i in crim_courts if request.GET.get("district_court: {}".format(i)) == i]
        circuit_courts = [i for i in crim_courts if request.GET.get("circuit_court: {}".format(i)) == i]

        combined_courts = district_courts + circuit_courts

        crim_resps = []
        for c in combined_courts:
            new_req = 'http://models-api:8000/spec/crim/?court={}&start_date={}&end_date={}'.format(c.replace(" ", "+"), req_details['start_date'], req_details['end_date'])
            resp = urllib.request.urlopen(new_req).read().decode('utf-8')
            resp = "[" + resp.replace("\'", "\"").replace("}{", "},{") + "]"
            resp = json.loads(resp)
            crim_resps.append(resp)

        if len(crim_resps) > 0:
            resps.append(('crim',crim_resps))

    responses = []

    output =  BytesIO()
    f = zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED)
    for name,i in resps:
        keys = i[0][0].keys()
        resper = StringIO()
        writer = csv.writer(resper)
        writer.writerow(keys)
        for j in i:
            for d in j:
                writer.writerow([d[k] for k in keys])
        resper.seek(0)
        f.writestr("{}.csv".format(name), resper.read())

    f.close()
    # Build your response
    response = HttpResponse(output.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="output.zip"'
    return response
