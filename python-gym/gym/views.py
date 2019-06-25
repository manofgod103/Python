import uuid

from django.core.cache import caches
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.conf import settings
from .models import StaffManager
# Create your views here.
user_cache = caches['user']
class UserViewSet(ViewSet):
    # data= {
    #     "username":"1434110813",
    #     "password":"123456",
    #     "role":3,
    #     "authority":1
    # }
    # user = StaffManager.create_user(data)

    @action(methods=["post"], detail=False)
    def login(self,request):
        username = request.data.get("username")
        password = request.data.get("password")
        role = int(request.data.get("role"))
        user = StaffManager.authenticate(username,password,role)
        if user:
            # print("进来了")
            token = uuid.uuid4().hex
            user_cache.set(token, user.pk, settings.USER_TOKEN_LIFE)
            return Response({"data": token})
        else:
            # 提示错误信息
            # print("出错了")
            return Response({"msg": "用户名或密码错误", "status": 3})
