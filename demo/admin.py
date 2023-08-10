from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import SysUser
from .models import Article
from .models import Project


admin.site.site_header = 'Django 管理后台(CODE)'
admin.site.site_title = 'Django 管理后台'


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'sex', 'age', 'created_at')
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('username',)


# 注册参数
admin.site.register(SysUser, UserAdmin)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'view_count', 'is_top', 'created_at', 'updated_at')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'project_desc', 'created_at', 'updated_at')
    list_display_links = ('project_name',)


admin.site.register(Project, ProjectAdmin)
