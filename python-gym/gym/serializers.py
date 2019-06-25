from rest_framework import serializers
from .models import *
from faker import Factory

class MemberRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberInfo
        fields = "__all__"

class MemberInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberInfo
        fields = ["username", "phone", "sex", "portrait"]

class MemberCardSerializer(serializers.ModelSerializer):
    member = MemberInfoSerializer()
    class Meta:
        model = MemberCard
        fields = ["member", "card_type", "end_time", "create_time", "use_time"]


class StaffInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffUserInfo
        fields = ["username", "number", "phone", "sex", "age", "department", "monthly_pay"]


class EquipmentModelSerializer(serializers.ModelSerializer):
    # buy_user = StaffInfoModelSerializer()
    class Meta:
        model = Equipment
        fields = ["equipment_name", "equipment_number", "buy_time", "repair_time", "equipment_status", "buy_user"]


# class EquipmentSerializer(serializers.Serializer):
#     equipment_name = serializers.CharField(
#         max_length=255
#     )
#     equipment_number = serializers.CharField(
#         max_length=255
#     )
#     buy_time = serializers.DateTimeField()
#     repair_time = serializers.DateTimeField()
#     equipment_status = serializers.IntegerField()
#     buy_user = StaffInfoModelSerializer()

    # @classmethod
    # def create_number(cls):
    #     fake = Factory.create("zh_CN")
    #     cls.equipment_number=fake.md5()
