#!/bin/bash

# 激活虚拟环境
# 如果没有虚拟环境，可以注释掉以下两行
# source /path/to/venv/bin/activate

# 切换到项目目录
cd /path/to/HipGo-VUE/backend

# 运行数据库迁移
python manage.py makemigrations
python manage.py migrate

# 创建超级用户（如果需要）
# python manage.py createsuperuser

# 启动 Django 开发服务器
python manage.py runserver

echo "Server is running on http://127.0.0.1:8000/"