__author__ = 'Yue Dayu'

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import os
from dilidili import settings
# from dilidili_dev.models import Video


class UserManager(BaseUserManager):
    def create_user(self, username, email, name, password, image=None, describe=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email=UserManager.normalize_email(email),
            username=username,
            name=name,
            describe=describe,
            money=100,
            is_admin=False)
        if image:
            user.image = image
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, name='admin', describe='describe'):
        user = self.create_user(
            email=email,
            username=username,
            name=name,
            describe=describe,
            password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=50, db_index=True)
    image = models.ImageField(
        upload_to='photos',
        default=os.path.join(settings.MEDIA_URL, 'photos', '001.jpg').replace('\\', '/')
    )
    describe = models.CharField(max_length=254, db_index=True)
    money = models.IntegerField(default=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # Permissions
    can_comment = models.BooleanField(default=True)
    can_upload = models.BooleanField(default=True)
    can_bullet = models.BooleanField(default=True)

    follow_users = models.ManyToManyField("User", related_name="following_users")
    like_videos = models.ManyToManyField("Video", related_name="like_videos")
    collection_videos = models.ManyToManyField("Video", related_name="collection_videos")

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
