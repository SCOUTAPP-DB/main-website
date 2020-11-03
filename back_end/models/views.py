from django.http import HttpResponse
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from .serializers import CivilCaseSerializer, CrimCaseSerializer
from .models import crim_case, civil_case
from rest_framework import viewsets
import json

def index(request):
    return HttpResponse("Hello World! This is the database site.")

class CivilCaseViewSet(viewsets.ViewSet):
    queryset = civil_case.objects.all()
    serializer_class = CivilCaseSerializer

    def list(self, request):
        queryset = civil_case.objects.all()
        serializer = CivilCaseSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CivilCaseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)

    def get_courts(self, request):
        """
        this API end point returns the distinct set of courts from the civil dataset
        """
        courts_civil = civil_case.objects.order_by('court').values('court').distinct()
        return Response(courts_civil)

    def get_specific_case(self, request):
        civil=True
        criminal=True

        req_details = { 
            'court':request.GET.get('court'),
            'start_date':request.GET.get('start_date') ,
            'end_date':request.GET.get('end_date') 
            }

        request_string = "SELECT * FROM models_civil_case WHERE court = '" + req_details['court'] + "' AND filed_date2 <= '" + req_details['end_date'] + "' AND filed_date2 >= '" + req_details['start_date'] + "';"
        cases = [civil_case.objects.raw(request_string)][0]
        cases = [i.__dict__ for i in cases]
        for i in cases:
            i.pop("_state")
            i.pop("filed_date2")
            i.pop("address")
        return HttpResponse(cases)

    def get_specific_case_test(self, request):
        civil=True
        criminal=True

        columns = [f.get_attname() for f in civil_case._meta.fields]
        req_details = { i:request.GET.get(i) for i in columns }

        request_string = "SELECT * FROM models_civil_case WHERE " +  " AND ".join(["{} = {}".format(i, req_details[i]) for i in req_details if req_details[i] != None]) + ";"
        cases = [civil_case.objects.raw(request_string)][0]
        cases = [i.__dict__ for i in cases]
        return HttpResponse(cases)

    def get_valid_columns(self, request):
        columns = [f.get_attname() for f in civil_case._meta.fields]
        return Response(columns)

    def get_unique_column_vals(self, request):

        req_details = {
            'column': request.GET.get("column"),
        }
        costs = civil_case.objects.order_by(req_details['column']).values(req_details['column']).distinct()
        return Response(costs)



class CrimCaseViewSet(viewsets.ViewSet):
    queryset = civil_case.objects.all()
    serializer_class = CrimCaseSerializer

    def list(self, request):
        queryset = crim_case.objects.all()
        serializer = CrimCaseSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CrimCaseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_courts(self, request):
        """
        this API end point returns the distinct set of courts from the criminal dataset
        """
        courts_criminal = crim_case.objects.order_by('court').values('court').distinct()
        return Response(courts_criminal)

    def get_specific_case(self, request):
        civil=True
        criminal=True

        req_details = { 
            'court':request.GET.get('court'),
            'start_date':request.GET.get('start_date') ,
            'end_date':request.GET.get('end_date') 
            }

        request_string = "SELECT * FROM models_crim_case WHERE court = '" + req_details['court'] + "' AND filed_date2 <= '" + req_details['end_date'] + "' AND filed_date2 >= '" + req_details['start_date'] + "';"
        cases = [crim_case.objects.raw(request_string)][0]
        cases = [i.__dict__ for i in cases]
        for i in cases:
            i.pop("_state")
            i.pop("filed_date2")
            i.pop("address")
        return HttpResponse(cases)

    def get_specific_case_teste(self, request):

        columns = [f.get_attname() for f in crim_case._meta.fields]
        req_details = { i:request.GET.get(i) for i in columns }

        request_string = "SELECT * FROM models_crim_case WHERE " +  " AND ".join(["{} = {}".format(i, req_details[i]) for i in req_details if req_details[i] != None]) + ";"
        cases = [crim_case.objects.raw(request_string)][0]
        cases = [i.__dict__ for i in cases]
        return HttpResponse(cases)

    def get_valid_columns(self, request):
        columns = [f.get_attname() for f in crim_case._meta.fields]
        return Response(columns)

    def get_unique_column_vals(self, request):

        req_details = {
            'column': request.GET.get("column"),
        }
        costs = crim_case.objects.order_by(req_details['column']).values(req_details['column']).distinct()
        return Response(costs)


  
