###代码结构说明:

目录`dilidili_dev/`:

`admin.py` 用户注册表单定义，重写的admin

`logout_in.py` 用户登陆、退出的view

`users.py` 用户及管理员model

目录`templates\`: 模板

目录`static\`: 静态文件，包括引用的css, javascript，图片等

目录`media\`: 储存上传的文件，包括头像图片、视频

`dilidili\dbs.py` 数据库设置。由于个人的数据库设置不同，将此文件从`setting.py`分离出。
