from django.db import models

# 王俊后勤系统
class StaffUserInfo(models.Model):
    SEX = (
        (1, "男"),
        (2, "女")
    )
    DEPARTMENT =(
        (1, "营销部"),
        (2, "行政部"),
        (3, "人事部"),
        (4, "后勤部"),
        (5, "财务部"),
    )
    username = models.CharField(
        max_length=20,
        verbose_name="姓名"
    )
    number = models.CharField(
        max_length=255,
        verbose_name="工号",
        unique=True,
        db_index=True
    )
    phone = models.CharField(
        max_length=11
    )
    sex = models.IntegerField(
        choices=SEX,
        verbose_name="性别"
    )
    age = models.IntegerField(

    )
    department = models.IntegerField(
        verbose_name="所属部门",
        choices=DEPARTMENT
    )
    monthly_pay = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        null=True
    )


class Equipment(models.Model):
    STATUS = (
        (1, "良好"),
        (2, "已损坏"),
        (3, "已维修"),
        (4, "已报废")
    )
    equipment_name = models.CharField(
        max_length=255
    )
    equipment_number = models.CharField(
        max_length=255,
        verbose_name="器材编号",
        unique=True,
        db_index=True
    )
    buy_time = models.DateTimeField(
        auto_created=True
    )
    repair_time = models.DateTimeField(
        null=True
    )
    equipment_status = models.IntegerField(
        choices=STATUS,
        default=1
    )
    buy_user = models.ForeignKey(
        StaffUserInfo
    )


# 超级管理员
class StaffManager(models.Model):
    ROLE= (
        (1,"前台"),
        (2, "后勤"),
        (3, "人事")
    )
    username = models.CharField(
        max_length=11,
        verbose_name="账号",
        unique=True,
        db_index=True
    )
    password =models.CharField(
        max_length=255
    )
    role = models.IntegerField(
        choices=ROLE,
        verbose_name="用户角色"
    )
    authority = models.BooleanField(
        default=0
    )

    @classmethod
    def make_password(cls,password):
        md5 = hashlib.md5()
        md5.update(password.encode())
        return md5.hexdigest().upper()

    @classmethod
    def create_user(cls, data):
        # 去检查用户名
        if cls.objects.filter(username=data.get("username")).exists():
            return None
        # 对密码做加密
        data["password"] = cls.make_password(data.get("password"))
        return cls.objects.create(**data)

    @classmethod
    def authenticate(cls, username=None, password=None, role=None):
        #         找人
        user = cls.objects.filter(
            username=username
        ).first()
        #         校验密码
        # print(user.role)
        # print(role)
        if user and user.password == cls.make_password(password) and user.role == role:
            return user

# 员工
class MemberInfo(models.Model):
    SEX = (
        (1, "男"),
        (2, "女")
    )
    username = models.CharField(
        max_length=20
    )
    phone = models.CharField(
        max_length=11,
        unique=True,
        db_index=True,
        verbose_name="手机号"
    )
    password = models.CharField(
        max_length=255,
        default="000000"
    )
    sex = models.IntegerField(
        choices=SEX,
        verbose_name="性别"
    )
    id_card = models.CharField(
        max_length=18
    )
    portrait = models.ImageField(
        max_length=255,
        verbose_name="头像"
    )
    transactor = models.ForeignKey(
        StaffUserInfo,
        null=True,
        blank=True
    )
