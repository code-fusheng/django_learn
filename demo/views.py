from django.shortcuts import render

# 视图层 V

# Create your views here.

from django.http import HttpResponse
from django.db import  connection
from demo import models
from datetime import datetime

from ninja import  Router
router = Router()

# 用户相关模块


def hello_get(request):
    print(request.path)
    print(request.get_full_path())
    print(request.method)
    print(request.GET.get('pageNum'))
    print(request.GET.get("pageSize"))
    return HttpResponse("Hello World")


def hello_post(request):
    print(request.path)
    print(request.method)
    print(request.body)
    return HttpResponse()


def index(request):
    user_index = models.SysUser.objects.all().order_by("-id")
    context = {
        'user_index': user_index,
    }
    return render(request, 'index.html', context)


def save_user(request):
    models.SysUser.objects.create(name='test', sex="男", age='1', created_at=datetime.now())
    return HttpResponse(True)


def delete_user(request):
    name = models.SysUser.objects.filter(id=3).delete()
    return HttpResponse(name)


def update_user(request):
    user = models.SysUser.objects.filter(id=1).update(name='code-fusheng/python')
    return HttpResponse(user)


# QuerySet API
def debug_project(request):
    # result = models.Project.objects.all()
    # result = models.Project.objects.values()
    # result = models.Project.objects.values_list()
    with connection.cursor() as cursor:
        cursor.execute('select * from demo_project')
        result = cursor.fetchall()
    return HttpResponse(result)


@router.get("/list")
def list_project():
    projects = models.Project.objects.all()
    return HttpResponse(projects)
