from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet


class TestViewSet(ModelViewSet):
    queryset = TestModel.objects.all()


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("codes", TestViewSet)
urlpatterns = router.urls
print(urlpatterns)
