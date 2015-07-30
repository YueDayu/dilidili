from django.db import models
from .users import *

#models
class Video(models.Model):
	name = models.CharField(max_length = 100)
	url = models.URLField()
	image = models.ImageField()#再check一下ImageField的PIL库版本支持问题
	describe = models.CharField(max_length = 200)
	tag = models.CharField(max_length = 84)#每个tag允许20个字符，每个视频允许添加4个tag，tag间用'#'分隔
	play = models.IntegerField()#播放次数
	money = models.IntegerField()#硬币数
	owner = models.OneToOneField(User)
	time = models.DateTimeField(auto_now=False, auto_now_add=True)#记录上传时间
	status = models.BooleanField()#审核中、已审核，要不要用IntegerField分出更多状态？

class Bullet(models.Model):
	video = models.ForeignKey(Video)
	user = models.ForeignKey(User)
	time = models.IntegerField()#记录添加时间，相对于视频开始时间的毫秒数。
	content = models.CharField(max_length = 200)
	color = models.CharField(max_length = 6)#就用6位16进制表示？

class Comment(models.Model):
	video = models.ForeignKey(Video)
	user = models.ForeignKey(User)
	content = models.CharField(max_length = 200)
	time = models.DateTimeField(auto_now=False, auto_now_add=True)

class Message(models.Model):
	user_from = models.ManyToManyField(User, related_name="user_from")
	user_to = models.ManyToManyField(User, related_name="user_to")
	status = models.BooleanField()
	time = models.DateTimeField(auto_now=False, auto_now_add=True)#记录创建时间

class Category(models.Model):
	name = models.CharField(max_length = 40)
	video_list = models.ManyToManyField(Video)

class Album(models.Model):
	name = models.CharField(max_length = 40)
	describe = models.CharField(max_length = 200)
	video_list = models.ManyToManyField(Video, through="AlbumVideo")

class AlbumVideo(models.Model):
	album = models.ForeignKey(Album)
	video = models.ForeignKey(Video)
	video_number = models.IntegerField() #video在album中的序号
