from rest_framework import serializers
from .models import VmTask, VmCurTask, VmTaskGroup


class VmTaskSer(serializers.ModelSerializer):
    class Meta:
        model = VmTask
        fields = ("task_name", "id", "is_ad", "user_type", "terminal_type")


class VmTaskGroupSer(serializers.ModelSerializer):
    task = VmTaskSer()

    class Meta:
        model = VmTaskGroup
        fields = ("id", "task_group_name", "times", "ran_times", "ranking", "task")
