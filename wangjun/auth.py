from django.core.cache import caches
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from .models import *


cache_user= caches["user"]
class StaffAuthentication(BaseAuthentication):

    def authenticate(self, request):
        # 前端要给我传token
        # 先通过get获取
        token= request.query_params.get("token")
        if not token:
            token=request.data.get("token")
        if not token:
            return None
        user_id=cache_user.get(token)
        try:
            user=MemberInfo.objects.get(pk=user_id)
        except Exception:
            try:
                user = StaffManager.objects.get(pk=user_id)
            except Exception:
                return None
        return user,token

class ManagerAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.query_params.get("token")
        if not token:
            token = request.data.get("token")
        if not token:
            raise exceptions.AuthenticationFailed("token参数缺失")
        user_id = cache_user.get(token)
        if user_id:
            try:
                user = StaffManager.objects.get(pk=user_id)
            except:
                raise exceptions.AuthenticationFailed("认证失败")
            return user,token
        else:
            raise exceptions.AuthenticationFailed("认证失败")

