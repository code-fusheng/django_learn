# Django 工程手册

## 一、工程创建

```shell
# 安装 Django
$ pip install django
```
> 注册应用 配置文件 Django_Learn/settings.py
```shell
INSTALLED_APPS = [
    "demo.apps.DemoConfig",    # 添加 app 应用
]
```

> 基础目录结构
```

```

> 项目目录配置文件介绍
```

```

> Django4.0 MVT 结构
模型(models):
视图(views):
模版(templates):

> 修改模型
1、在models.py中修改模型；
2、运行python manage.py makemigrations为改动创建迁移记录；
3、运行python manage.py migrate，将操作同步到数据库。


## 二、常用指令
```shell
# 新建项目
$ django-admin.py startproject Django_Learn
# 新建应用
$ python manage.py startapp demo
# 启动服务
$ python manage.py runserver 8080
# Django 命令查看
$ 
# 数据库迁移
$ python manage.py makemigrations
$ python manage.py migrate
# 创建管理员
$ python manage.py createsuperuser
- Username: admin
- Password: ******

# 导出依赖
$ pip freeze > requirements.txt
# 安装依赖
$ pip install -r requirements.txt 

```

## 三、全局配置 setting
### 1. 静态文件配置
> 配置静态文件
STATIC_URL = "static/"  # 静态文档别名
> 静态文件地址拼接 static 文件为自己创建的存放静态文件的文件夹名
```shell
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),  # 主文件下静态文件
    os.path.join(BASE_DIR, "demo", "statics")   # 项目 demo 文件下静态文件
)
```
### 2. 全局日志配置
```shell
# 设置日志打印
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        }
    }
}
```


### 3. SQL 语句日志配置
```shell
LOGGING = {
  'version': 1,
  'disable_existing_loggers': Flase,
  'handlers': {
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler'
    }
  },
  'loggers': {
    'django.db.backends': {
      'handlers': ['console'],
      'propagate': True,
      'level': 'DEBUG',
    },
  }
}
```

### 4. 继承内置 AbstractUser
> 1. 引入 model
```shell
from django.contrib.auth.models import AbstractUser
```

> 2. 配置 setting
```shell
AUTH_USER_MODEL = '应用名.User'
```

