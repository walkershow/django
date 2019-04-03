from django import setup
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_learn.settings")
setup()

from rest_framework import serializers
from rest_learn.models import VmTask, VmTaskGroup, VmCurTask
from django.forms.models import model_to_dict


class TestSOne(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    agedd = serializers.IntegerField()


class VmTaskSer(serializers.ModelSerializer):
    class Meta:
        model = VmTask
        fields = "__all__"


class TestForeignSer(serializers.ModelSerializer):
    task = VmTaskSer()

    class Meta:
        model = VmTaskGroup
        fields = "__all__"


t = TestForeignSer(data=VmTaskGroup.objects.all())
print(t.initial_data[0].task.task_name)
# if t.is_valid():
# print(t.validated_data)
# print(t.errors)

# data = {"name": "heklll", "age": 100}
# t = TestSOne(data=data)
# if t.is_valid():
# print(t.validated_data)
# print(t.errors)
