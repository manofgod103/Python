from .auth import LoginMiniAuthentication
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import MemberRegisterSerializer, MemberCardSerializer, MemberInfoSerializer
from .models import *

# 会员注册
class MemberInfoViewSet(ViewSet):

    @action(methods=["post"], detail=False)
    def member_register(self,req):
        # print("进来了")
        username = req.data.get("username")
        phone = req.data.get("phone")
        id_card = int(req.data.get("id_card"))
        card_type = req.data.get("card_type")
        sex = int(req.data.get("sex"))
        transactor = req.data.get("transactor")
        if transactor =="":
            transactor = None
        data1 = {
            "username":username,
            "phone":phone,
            "id_card":id_card,
            "sex":sex,
            "transactor_id":transactor
        }
        member =MemberInfo.objects.create(**data1)
        if member:
            data2= {
                "card_type":card_type,
                "member_id":member
            }
            member_card = MemberCard.objects.create(**data2)
            # print(member_card)
            if member_card:
                return Response({})
            else:
                return Response({"status": 2, "msg": "创建失败"})
        else:
            return Response({"status": 2, "msg": "创建失败"})
# 会员信息列表
class MemberInfoAPIView(ListAPIView):
    queryset = MemberInfo.objects.all()
    serializer_class = MemberInfoSerializer
    authentication_classes = [LoginMiniAuthentication]
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# 注销会员
class EditMemberInfo(ViewSet):

    authentication_classes = [LoginMiniAuthentication]
    @action(methods=["post"], detail=False)
    def delete(self,request):
        user = request.user
        print(user)
        member_id = request.data.get("member_id")
        print(member_id)
        print()
        if user.authority == 1:
            member = MemberInfo.objects.filter(pk=member_id)
            member.delete()
            return Response({"msg":"注销成功"})
        else:
            return Response({"status":10, "msg":"您没有权限进行此操作"})

# 修改会员信息
class UpdateMemberInfo(UpdateAPIView):
    authentication_classes = [LoginMiniAuthentication]

    def put(self, request, *args, **kwargs):
        user = request.user
        member_id = request.data.get("member_id")
        username = request.data.get("username")
        phone = request.data.get("phone")
        sex = int(request.data.get("sex"))
        portrait = request.data.get("portrait")
        member = MemberInfo.objects.filter(pk=member_id).first()
        if user:
            member.username = username
            member.phone = phone
            member.sex = sex
            member.portrait = portrait
            member.save()
            return Response({"msg":"修改成功"})

# 查询某个会员的所有信息
class SearchMemberAPIView(ListAPIView):
    authentication_classes = [LoginMiniAuthentication]
    serializer_class = MemberCardSerializer
    # queryset = MemberCard.objects.all()

    def list(self, request, *args, **kwargs):
        user =request.user
        phone = request.query_params.get("phone")
        member = MemberInfo.objects.filter(phone=phone).first()
        queryset = MemberCard.objects.filter(member=member)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"data":serializer.data})

# 会员继续办会员卡
class MemberContinuityCard(ViewSet):
    authentication_classes = [LoginMiniAuthentication]

    @action(methods=["post"], detail=False)
    def again(self,request):
        member_id = request.data.get("member_id")
        card_type = request.data.get("card_type")
        member = MemberInfo.objects.filter(pk=member_id).first()
        data = {
            "card_type": card_type,
            "member_id": member
        }
        member_card = MemberCard.objects.create(**data)
        if member_card:
            return Response({"msg":"再次办理会员卡成功"})
        else:
            return Response({"status":"11", "msg":"办理失败"})








