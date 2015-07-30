from django.db import models
from dilidili_dev.users import User

# models
# 视频model
class Video(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos')
    image = models.ImageField()
    describe = models.CharField(max_length=200)
    tag = models.CharField(max_length=84)  # 每个tag允许20个字符，每个视频允许添加4个tag，tag间用'#'分隔
    play = models.IntegerField(default=0)  # 播放次数
    money = models.IntegerField(default=0)  # 硬币数
    owner = models.OneToOneField('User')
    time = models.DateTimeField(auto_now=False, auto_now_add=True)  # 记录上传时间
    status = models.IntegerField(default=0)  # 审核中0、已审核1、禁播2


# 弹幕
class Bullet(models.Model):
    video = models.ForeignKey('Video')
    user = models.ForeignKey('User')
    time = models.IntegerField(default=0)  # 记录添加时间，相对于视频开始时间的帧数。
    send_date = models.DateTimeField(auto_now=False, auto_now_add=True)  # 上传时间，用来判断轮询
    content = models.CharField(max_length=200)
    color = models.CharField(max_length=10)  # 弹幕颜色


# 评论
class Comment(models.Model):
    video = models.ForeignKey('Video')
    user = models.ForeignKey('User')
    content = models.CharField(max_length=400)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)


# 私信
class Message(models.Model):
    user_from = models.ManyToManyField('User', related_name="user_from")
    user_to = models.ManyToManyField('User', related_name="user_to")
    status = models.BooleanField(default=False)  # 已读 未读
    time = models.DateTimeField(auto_now=False, auto_now_add=True)  # 记录创建时间


# 分类 默认，一般不建立
class Category(models.Model):
    name = models.CharField(max_length=40)
    video_list = models.ManyToManyField('Video')


# 专辑
class Album(models.Model):
    image = models.ImageField()
    money = models.IntegerField(default=0)  # 硬币数，计算从专辑页面加硬币的情况
    owner = models.OneToOneField('User')
    time = models.DateTimeField(auto_now=False, auto_now_add=True)  # 记录上传时间
    name = models.CharField(max_length=40)
    describe = models.CharField(max_length=200)
    video_list = models.ManyToManyField('Video', through="AlbumVideo")


# 专辑--视频关系
class AlbumVideo(models.Model):
    album = models.ForeignKey('Album')
    video = models.ForeignKey('Video')
    video_number = models.IntegerField()  # video在album中的序号


# 首页视频
class BestVideo(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    video = models.OneToOneField('Video')
