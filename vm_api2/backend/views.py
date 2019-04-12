from django.db import models
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import VmTaskSer, VmTaskGroupSer
from .models import VmTask, VmTaskGroup
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication
from django.http import HttpResponseNotFound, HttpResponse


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


# Create your views here.


class TaskViewSet(ModelViewSet):
    queryset = VmTaskGroup.objects.filter(task__status=1, times__gt=0).order_by(
        "-ran_times", "-times"
    )
    # queryset = VmTaskGroup.objects.all()
    serializer_class = VmTaskGroupSer
    # authentication_classes = (CsrfExemptSessionAuthentication,)

    def list(self, request, *args, **kwargs):
        serializer = VmTaskGroupSer(self.get_queryset(), many=True)
        headers = {}
        headers["Access-Control-Allow-Origin"] = "*"
        return Response(data=serializer.data, headers=headers)

    def retrieve(self, request, pk=None):

        # task = get_object_or_404(self.get_queryset(), pk=pk)
        data = VmTaskGroup.objects.filter(pk=pk)
        # print("data.id", data[0].id)
        # print("data", data)
        # print ()
        if data:
            serializer = VmTaskGroupSer(data, many=True)


def home(request):
    with open("frontend/index.html", "rb") as f:
        content = f.read()
    return HttpResponse(content)


def js(request, filename):
    with open("frontend/{}".format(filename), "rb") as f:
        js_content = f.read()
    return HttpResponse(content=js_content, content_type="application/javascript")


def css(request, filename):
    with open("frontend/{}".format(filename), "rb") as f:
        css_content = f.read()
    return HttpResponse(content=css_content, content_type="text/css")
