from django.shortcuts import render

""" view 视图 """

# 基础 drf 提供路由
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
#
from rest_framework.permissions import BasePermission
# 认证组件
from rest_framework.authentication import BaseAuthentication
from users import models

class MinePermission(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        # 视图中 self.get_object()
        return True

# 序列化器
class DepartSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Depart
        fields = "__all__"

class DepartView(ModelViewSet):
    queryset = models.Depart.objects.all()
    serializer_class = DepartSerializers

    permission_classes = [MinePermission, ]