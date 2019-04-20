from rest_framework import serializers
from .models import VmTask, VmCurTask, VmTaskGroup, VmTaskAllotImpl
from django.db.models.functions import Now


class VmTaskSer(serializers.ModelSerializer):
    # user_type = serializers.ChoiceField(((0, "baidu"), (1, "360")))
    # user_type = serializers.CharField(max_length=2, choices=((0, "baidu"), (1, "360")))
    # user_type = serializers.CharField(max_length=2, choices=((0, "baidu"), (1, "360")))
    # user_type = EnumChoiceField(enum_class=UserType)

    class Meta:
        model = VmTask
        fields = (
            "task_name",
            "id",
            "get_is_ad_display",
            "get_user_type_display",
            "get_terminal_type_display",
            "is_ad",
            "user_type",
            "terminal_type",
            "inter_time",
            "status",
        )
        # 如果没有这个会校验不通过
        extra_kwargs = {"id": {"validators": []}}


class VmTaskGroupSer(serializers.ModelSerializer):
    task = VmTaskSer()

    class Meta:
        model = VmTaskGroup
        fields = ("id", "task_group_name", "times", "ran_times", "ranking", "task")
        extra_kwargs = {"id": {"validators": []}}

    def create(self, instance, validated_data):
        print("create instance")
        return instance

    def update(self, instance, validated_data):
        task_data = validated_data.pop("task")
        task_id = task_data["id"]
        VmTask.objects.filter(pk=task_id).update(status=task_data["status"])
        # VmTask.objects.filter(pk=task_id).update(**task_data)
        # task_object = VmTask.objects.get(pk=task_id)

        # task_object = VmTask(id=task_id, status=task_data["status"])
        # print("task_object", task_object)
        # task_object.status = task_data.get("status", task_object.status)
        # task_object2.save()
        print("task-id", task_id)
        print("update task", task_data)
        print("instance", instance)
        instance.task_group_name = validated_data.get(
            "task_group_name", instance.task_group_name
        )
        instance.times = validated_data.get("times", instance.times)
        instance.ran_times = validated_data.get("ran_times", instance.ran_times)
        instance.ranking = validated_data.get("ranking", instance.ranking)
        # instance.task = task_object
        # print("task status", task_data.get("status"))
        # instance.task.status = task_data.get("status", 0)
        instance.save()
        # tasks = (instance.task).objects.all()
        # print("tasks", tasks)
        if task_data["status"] == 1:
            VmTaskAllotImpl.objects.filter(
                task_id=task_id, start_time__lt=Now()
            ).update(is_done=1)
        return instance
