from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response

from .models import *
from .serializers import EquipmentModelSerializer
from .auth import StaffAuthentication,ManagerAuthentication

# 获取所有数据，前提要先认证通过
class EquipmentListAPIView(ListAPIView):
    authentication_classes = [StaffAuthentication]
    queryset = Equipment.objects.all()
    serializer_class = EquipmentModelSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "code":200,
            "msg":"OK",
            "data":serializer.data
        })


# 通过id获取单条数据
class EquipmentRetrieveAPIView(RetrieveAPIView):
    authentication_classes = [StaffAuthentication]
    queryset = Equipment.objects.all()
    serializer_class = EquipmentModelSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "code":200,
            "msg":"OK",
            "data":serializer.data
        })

# 通过id修改某条数据
class EquipmentUpdateAPIView(UpdateAPIView):
    authentication_classes = [ManagerAuthentication]
    queryset = Equipment.objects.all()
    serializer_class = EquipmentModelSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response({
            "code":200,
            "msg":"OK",
            "data":serializer.data
        })

# 创建数据
class EquipmentCreateAPIView(CreateAPIView):
    pass






