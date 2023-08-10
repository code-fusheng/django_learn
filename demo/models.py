from django.db import models

# 数据层 M

# Create your models here.
# Django 要求模型必须继承 models.Model

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class SysUser(AbstractUser):
    name = models.CharField('姓名', max_length=20)
    sex = models.CharField('性别', max_length=2, blank=True)
    age = models.IntegerField('年龄')
    created_at = models.DateTimeField('发布时间', auto_now_add=True)

    class Meta:
        verbose_name = '用户',
        verbose_name_plural = '用户'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    keywords = models.CharField('关键字', max_length=120, blank=True, null=True)
    abstract = models.TextField('摘要', max_length=200, blank=True)
    category = models.CharField('分类', max_length=20, blank=True)
    content = models.TextField('内容')
    author = models.CharField('作者', max_length=20)
    view_count = models.IntegerField('阅读量', default=0)
    is_top = models.IntegerField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='是否推荐')
    created_at = models.DateTimeField('发布时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '文章',
        verbose_name_plural = '文章',

    def __str__(self):
        return self.title


class Project(models.Model):
    project_name = models.CharField('项目名称', max_length=50)
    project_desc = models.CharField('项目描述', max_length=500, blank=True)
    is_enabled = models.IntegerField('是否启用', choices=[(0, '未启用'), (1, '已启用')], default=1)
    is_deleted = models.IntegerField('是否逻辑删除', choices=[(0, '未删除'), (1, '已删除')], default=0)
    created_at = models.DateTimeField('发布时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '项目',
        verbose_name_plural = '项目'

    def __str__(self):
        return self.project_name





