from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
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


class GetValidTaskView(ListMixin, APIView):
    def get(self, *args, **kwargs):
        self.queryset = VmTaskGroup.objects.filter(task__status=1).order_by("-times")
        return self.list()


# 主页视图
def home(request):
    """
    读取 'index.html' 并返回响应
    :param request: 请求对象
    :return: HttpResponse
    """
    with open("frontend/index.html", "rb") as f:
        content = f.read()
    return HttpResponse(content)


# 读取 js 视图
def js(request, filename):
    """
    读取 js 文件并返回 js 文件响应
    :param request: 请求对象
    :param filename: str-> 文件名
    :return: HttpResponse
    """
    with open("frontend/js/{}".format(filename), "rb") as f:
        js_content = f.read()
        print(js_content)
    return HttpResponse(
        content=js_content, content_type="application/javascript"
    )  # 返回 js 响应


# 读取 css 视图
def css(request, filename):
    """
    读取 css 文件，并返回 css 文件响应
    :param request: 请求对象
    :param filename: str-> 文件名
    :return: HttpResponse
    """
    with open("frontend/css/{}".format(filename), "rb") as f:
        css_content = f.read()
    return HttpResponse(content=css_content, content_type="text/css")  # 返回 css 响应
