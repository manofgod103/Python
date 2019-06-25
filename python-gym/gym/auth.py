from django.core.cache import caches
from rest_framework.authentication import BaseAuthentication
from .models import StaffManager,MemberInfo
from rest_framework import exceptions

user_cache = caches["user"]
class LoginAuthentication(BaseAuthentication):

    def authenticate(self, request):
        # 先获取token
        token = request.query_params.get("token")
        if not token:
            token = request.data.get("token")
        if not token:
            raise exceptions.AuthenticationFailed("token参数缺失")
        # 去缓存找数据"token
        user_id = user_cache.get(token)
        # 如果找到返回用户和token
        if user_id:
            user = StaffManager.objects.get(pk=user_id)
            return user, token
        # 如果没找到 抛出异常
        else:

            raise exceptions.AuthenticationFailed("认证失败请先登录")

class LoginMiniAuthentication(BaseAuthentication):

    def authenticate(self, request):
        # 先获取token
        token = request.query_params.get("token")
        if not token:
            token = request.data.get("token")
        if not token:
            return None
        # 去缓存找数据"token
        user_id = user_cache.get(token)
        # 如果找到返回用户和token
        if user_id:
            user = StaffManager.objects.get(pk=user_id)
            return user, token
        # 如果没找到 抛出异常
        else:
            return None


class StaffAuthentication(BaseAuthentication):

    def authenticate(self, request):
        # 前端要给我传token
        # 先通过get获取
        token= request.query_params.get("token")
        if not token:
            token=request.data.get("token")
        if not token:
            return None
        user_id=user_cache.get(token)
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
        user_id = user_cache.get(token)
        if user_id:
            try:
                user = StaffManager.objects.get(pk=user_id)
            except:
                raise exceptions.AuthenticationFailed("认证失败")
            return user,token
        else:
            raise exceptions.AuthenticationFailed("认证失败")

