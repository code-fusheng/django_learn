# Generated by Django 2.2.28 on 2023-08-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='名称')),
                ('count', models.IntegerField(verbose_name='人数')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('remark', models.TextField(blank=True)),
                ('role', models.CharField(choices=[('admin', '管理员'), ('user', '用户'), ('test', '测试')], default='user', max_length=20, verbose_name='角色')),
            ],
        ),
    ]
