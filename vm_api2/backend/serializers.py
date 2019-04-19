from rest_framework import serializers
from .models import VmTask, VmCurTask, VmTaskGroup


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

    def update(self, instance, validated_data):
        task = validated_data.pop("task")
        task_id = task["id"]
        print("task-id", task_id)
        print("update task", task)
        print("instance", instance)
        instance.task_group_name = validated_data.get(
            "task_group_name", instance.task_group_name
        )
        instance.times = validated_data.get("times", instance.times)
        instance.ran_times = validated_data.get("ran_times", instance.ran_times)
        instance.ranking = validated_data.get("ranking", instance.ranking)
        instance.save()
        # tasks = (instance.task).objects.all()
        # print("tasks", tasks)
        task_object = VmTask.objects.get(pk=task_id)
        print("task_object", task_object)
        task_object.status = task.get("status", task_object.status)
        task_object.save()
        return instance
