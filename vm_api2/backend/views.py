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
    queryset = VmTaskGroup.objects.filter(times__gt=0).order_by("-ran_times", "-times")
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
        print("pk:", pk)
        data = VmTaskGroup.objects.filter(pk=pk)
        print("data:", data)
        # print("data.id", data[0].id)
        # print("data", data)
        # print ()
        if data:
            serializer = VmTaskGroupSer(data, many=True)
            headers = {}
            headers.setdefault("Access-Control-Allow-Origin", "*")
            # headers["Access-Control-Allow-Origin"] = "*"
            return Response(data=serializer.data, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print("Instance:", instance)
        print("instance id, name", instance.id, instance.task_group_name)
        serializer = self.serializer_class(instance, data=request.data)
        print("request.data", request.data)
        if serializer.is_valid():
            # print("serializer data", serializer.data)
            serializer.save()
            return Response(
                data=serializer.validated_data, status=status.HTTP_201_CREATED
            )
        print("serialize error:", serializer.errors)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # id = request.data["id"]
    # task_group_name = request.data["task_group_name"]
    # instance = self.get_object()
    # tasks = instance.task
    # instance.id = id
    # instance.task_group_name = task_group_name
    # print("task:", tasks)
    # instance.save()
    # return Response(data={"message": "ok"}, status=status.HTTP_201_CREATED)


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
