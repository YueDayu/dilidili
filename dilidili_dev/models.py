from django.db import models
from dilidili_dev.users import User
from dilidili import settings
import os

# models
# 视频模型
class Video(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos')
    image = models.ImageField(
        upload_to='images',
        default=os.path.join('photos', '001.jpg').replace('\\', '/')
    )
    describe = models.CharField(max_length=200)
    tag = models.CharField(max_length=84, default="",
                           blank=True)  # 标签
    category_set = models.ManyToManyField('Category', blank=True)
    play = models.IntegerField(default=0)  # 播放次数
    money = models.IntegerField(default=0)  # 硬币数量
    owner = models.ForeignKey('User')
    time = models.DateTimeField(auto_now=False, auto_now_add=True)  # 时间
    status = models.IntegerField(default=0)  # 视频状态

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/video/%u' % self.pk


# 弹幕
class Bullet(models.Model):
    video = models.ForeignKey('Video')
    user = models.ForeignKey('User')
    time = models.IntegerField(default=0)  # 视频的帧数
    send_date = models.DateTimeField(auto_now=False, auto_now_add=True)  # 发送时间
    content = models.CharField(max_length=200)
    color = models.CharField(max_length=10)  # 颜色


# 评论
class Comment(models.Model):
    video = models.ForeignKey('Video')
    user = models.ForeignKey('User')
    content = models.CharField(max_length=400)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)


# 私信
class Message(models.Model):
    user_from = models.ForeignKey('User', related_name="msg_send")
    user_to = models.ForeignKey('User', related_name="msg_receive")
    content = models.CharField(max_length=400)
    status = models.BooleanField(default=False)  # 已读未读
    time = models.DateTimeField(auto_now=False, auto_now_add=True)  # 发送时间


# 分类
class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/category/%u' % self.pk


# 专辑
class Album(models.Model):
    image = models.ImageField()
    money = models.IntegerField(default=0)  # 专辑创建以来的硬币数
    owner = models.ForeignKey('User')
    time = models.DateTimeField(auto_now=False, auto_now_add=True)  # 上传时间
    name = models.CharField(max_length=40)
    describe = models.CharField(max_length=200)
    video_list = models.ManyToManyField('Video', through="AlbumVideo")


# 视频--专辑关系
class AlbumVideo(models.Model):
    album = models.ForeignKey('Album')
    video = models.ForeignKey('Video')
    video_number = models.IntegerField()  # 视频在专辑中的序号


# 最佳视频
class BestVideo(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(
        upload_to='images',
        default=os.path.join('photos', '001.jpg').replace('\\', '/')
    )
    video = models.ForeignKey('Video')
