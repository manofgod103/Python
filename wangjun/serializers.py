from rest_framework import serializers
from .models import Equipment, StaffUserInfo
from faker import Factory

class StaffInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffUserInfo
        fields = ["username", "number", "phone", "sex", "age", "department", "monthly_pay"]


class EquipmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ["equipment_name", "equipment_number", "buy_time", "repair_time", "equipment_status", "buy_user"]


class EquipmentSerializer(serializers.Serializer):
    equipment_name = serializers.CharField(
        max_length=255
    )
    equipment_number = serializers.CharField(
        max_length=255
    )
    buy_time = serializers.DateTimeField()
    repair_time = serializers.DateTimeField()
    equipment_status = serializers.IntegerField()
    buy_user = serializers.IntegerField()

    @classmethod
    def create_number(cls):
        fake = Factory.create("zh_CN")
        cls.equipment_number=fake.md5()
