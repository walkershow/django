from django import setup
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_learn.settings")
setup()

from rest_framework import serializers


class TestSOne(serializers.Serializer):
    name = serializers.CharField(max_length=20)


data = {"name": "heklll", "age": "100"}
t = TestSOne(data=data)
if t.is_valid():
    print(t.validate_data())
