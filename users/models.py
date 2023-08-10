from django.db import models

# Create your models here.
# 创建应用程序：使用python manage.py startapp users命令创建一个名为"users"的新应用程序。
# 迁移数据库：运行python manage.py makemigrations和python manage.py migrate命令，将用户模型的更改应用于数据库。
# 注册用户模型：在"users/admin.py"文件中，注册用户模型以在Django管理界面中显示和编辑用户信息。

from django.contrib.auth.models import AbstractUser
from django.db import models

class UserInfo(models.Model):

    # username \ first_name \ last_name \ email \ is_staff \ is_active \ date_joined
    # 添加自定义拓展字段

    username = models.CharField(verbose_name="用户名", max_length=50)
    password = models.CharField(verbose_name="密码", max_length=255)
    remark = models.TextField(blank=True)

    role_choices = (
        ("admin", "管理员"),
        ("user", "用户"),
        ("test", "测试")
    )

    role = models.CharField(verbose_name="角色", max_length=20, choices=role_choices, default="user")

    def __str__(self):
        return self.username


class Depart(models.Model):
    """ 部门表 """
    title = models.CharField(verbose_name="名称", max_length=50)
    count = models.IntegerField(verbose_name="人数")