import time

import shortuuid
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from .models import *
from .serializers import EquipmentModelSerializer
from .auth import StaffAuthentication,LoginAuthentication,ManagerAuthentication

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
        return Response(serializer.data)


# 通过id获取单条数据
class EquipmentRetrieveAPIView(RetrieveAPIView):
    authentication_classes = [StaffAuthentication]
    # queryset = Equipment.objects.all()
    serializer_class = EquipmentModelSerializer

    def retrieve(self, request, *args, **kwargs):
        id = request.data.get("id")

        instance = Equipment.objects.get(pk=id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

# 通过id修改某条数据
class EquipmentUpdateAPIView(UpdateAPIView):
    authentication_classes = [LoginAuthentication]
    serializer_class = EquipmentModelSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        id = request.data.get("id")

        instance = Equipment.objects.get(pk=id)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

# 创建数据
class EquipmentCreateAPIView(CreateAPIView):
    authentication_classes = [StaffAuthentication]
    serializer_class = EquipmentModelSerializer

    def create(self, request, *args, **kwargs):
        id =request.data.get("id")
        user = StaffUserInfo.objects.filter(pk=id)

        data =request.data
        #修改QueryDict
        _mutable = data._mutable
        data._mutable = True
        # print(data["id"])
        data["buy_user"]=user
        num = shortuuid.uuid()
        data["equipment_number"]=num
        if "id" in data:
            data.pop("id")
        data._mutable = _mutable
        # 修改完成
        print(data)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)





# 删除数据
class EquipmentDestroyAPIView(DestroyAPIView):
    # 超级管理员可以删除
    authentication_classes = [ManagerAuthentication]

    def destroy(self, request, *args, **kwargs):
        id = request.data.get("id")
        instance = Equipment.objects.get(pk=id)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



