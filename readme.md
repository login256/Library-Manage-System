## 依赖

本网站有Django框架构建

需要的python版本为`3.8`

需要的包有：

```
Django
django-crispy-forms
```

## 快速部署

部署时如果不需要改变数据库后端，则可直接运行一下命令部署：

```shell
python3 -m pip install Django django-crispy-forms
python3 ./manage.py migrate
python3 ./manage.py runserver
```

