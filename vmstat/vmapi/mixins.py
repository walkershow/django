from django.db import models, IntegrityError
import subprocess
from django.http import Http404


class QuerysetMixin(object):
    model = None
    queryset = None

    def get_queryset(self):
        assert self.model or self.queryset, "no queryset found"
        if self.queryset:
            return self.queryset
        else:
            return self.model.objects.all()


class ListMixin(QuerysetMixin):
    def list(self, fields=None):
        print(self.get_queryset())
        return self.response(queryset=self.get_queryset(), fields=fields)
