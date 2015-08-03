from django.db import models
from dilidili_dev.users import User
from dilidili import settings
import os

# models
# ÊÓÆµmodel
class Video(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos')
    image = models.ImageField(
        upload_to='images',
        default=os.path.join(settings.MEDIA_URL, 'photos', '001.jpg').replace('\\', '/')
    )
    describe = models.CharField(max_length=200)
    tag = models.CharField(max_length=84, default="", blank=True)  # Ã¿¸ötagÔÊÐí20¸ö×Ö·û£¬Ã¿¸öÊÓÆµÔÊÐíÌí¼Ó4¸ötag£¬tag¼äÓÃ'#'·Ö¸ô
    category_set = models.ManyToManyField('Category', blank=True)
    play = models.IntegerField(default=0)  # ²¥·Å´ÎÊý
    money = models.IntegerField(default=0)  # Ó²±ÒÊý
    owner = models.ForeignKey('User')
    time = models.DateTimeField(auto_now=False, auto_now_add=True)  # ¼ÇÂ¼ÉÏ´«Ê±¼ä
    status = models.IntegerField(default=0)  # ÉóºËÖÐ0¡¢ÒÑÉóºË1¡¢½û²¥2


# µ¯Ä»
class Bullet(models.Model):
    video = models.ForeignKey('Video')
    user = models.ForeignKey('User')
    time = models.IntegerField(default=0)  # ¼ÇÂ¼Ìí¼ÓÊ±¼ä£¬Ïà¶ÔÓÚÊÓÆµ¿ªÊ¼Ê±¼äµÄÖ¡Êý¡£
    send_date = models.DateTimeField(auto_now=False, auto_now_add=True)  # ÉÏ´«Ê±¼ä£¬ÓÃÀ´ÅÐ¶ÏÂÖÑ¯
    content = models.CharField(max_length=200)
    color = models.CharField(max_length=10)  # µ¯Ä»ÑÕÉ«


# ÆÀÂÛ
class Comment(models.Model):
    video = models.ForeignKey('Video')
    user = models.ForeignKey('User')
    content = models.CharField(max_length=400)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)


# Ë½ÐÅ
class Message(models.Model):
    user_from = models.ManyToManyField('User', related_name="user_from")
    user_to = models.ManyToManyField('User', related_name="user_to")
    status = models.BooleanField(default=False)  # ÒÑ¶Á Î´¶Á
    time = models.DateTimeField(auto_now=False, auto_now_add=True)  # ¼ÇÂ¼´´½¨Ê±¼ä


# ·ÖÀà Ä¬ÈÏ£¬Ò»°ã²»½¨Á¢
class Category(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name


# ×¨¼­
class Album(models.Model):
    image = models.ImageField()
    money = models.IntegerField(default=0)  # Ó²±ÒÊý£¬¼ÆËã´Ó×¨¼­Ò³Ãæ¼ÓÓ²±ÒµÄÇé¿ö
    owner = models.ForeignKey('User')
    time = models.DateTimeField(auto_now=False, auto_now_add=True)  # ¼ÇÂ¼ÉÏ´«Ê±¼ä
    name = models.CharField(max_length=40)
    describe = models.CharField(max_length=200)
    video_list = models.ManyToManyField('Video', through="AlbumVideo")


# ×¨¼­--ÊÓÆµ¹ØÏµ
class AlbumVideo(models.Model):
    album = models.ForeignKey('Album')
    video = models.ForeignKey('Video')
    video_number = models.IntegerField()  # videoÔÚalbumÖÐµÄÐòºÅ


# Ê×Ò³ÊÓÆµ
class BestVideo(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    video = models.ForeignKey('Video')
