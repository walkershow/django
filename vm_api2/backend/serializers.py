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
            "inter_time",
        )


class VmTaskGroupSer(serializers.ModelSerializer):
    task = VmTaskSer()

    class Meta:
        model = VmTaskGroup
        fields = ("id", "task_group_name", "times", "ran_times", "ranking", "task")
