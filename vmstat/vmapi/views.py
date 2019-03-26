from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import VmCurTask, VmTask, VmTaskGroup
from .mixins import QuerysetMixin, ListMixin
import json
import datetime

# Create your views here.
class APIView(View):
    def response(self, queryset=None, fields=None, **kwargs):
        print(queryset)
        if queryset and fields:
            s_data = serialize(format="json", queryset=queryset, fields=fields)
        elif queryset:
            s_data = serialize(format="json", queryset=queryset)
        else:
            s_data = None

        instances = json.loads(s_data) if s_data else "no instances"
        data = {"instances": instances}

        data.update(kwargs)
        print(data)
        # todo
        # test the data output
        return JsonResponse(data=data)


class GetTasklistView(ListMixin, APIView):
    # model = VmCurTask

    def get(self, *args, **kwargs):
        from django.utils import timezone

        # https://zhuanlan.zhihu.com/p/30256210
        print(timezone.now().date())
        self.queryset = VmCurTask.objects.filter(start_time__lt=timezone.now())[:10]
        # return {"a:1"}
        # return self.response(status="succ")
        return self.list()
