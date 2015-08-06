"""dilidili URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import dilidili.settings as settings

urlpatterns = [
    url(r'^$', 'dilidili_dev.views.index'),
    url(r'^category/(?P<category_id>[0-9]+)', 'dilidili_dev.views.category_index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', 'dilidili_dev.views.register'),
    url(r'^logout/', 'dilidili_dev.logout_in.logout'),
    url(r'^login/', 'dilidili_dev.logout_in.login'),
    url(r'^personal/(?P<user_id>[0-9]+)/', include('dilidili_dev.admin_user_urls')),
    url(r'^video/(?P<video_id>[0-9]+)/', include([
        url(r'^$', 'dilidili_dev.video_play.video_play'),
        url(r'^remove/$', 'dilidili_dev.admin_video.remove'),
        url(r'^togglepublish/$', 'dilidili_dev.admin_video.togglepublish')
    ])),
    url(r'^video-add-play/$', 'dilidili_dev.views.video_play_add'),
    url(r'^video-add-bullet/$', 'dilidili_dev.video_play.video_bullet_add'),
    url(r'^video-add-comment/$', 'dilidili_dev.video_play.video_comment_add'),
    url(r'^video-get-bullet/$', 'dilidili_dev.video_play.video_bullet_get'),
    url(r'^video-get-comment/$', 'dilidili_dev.video_play.get_video_comment'),
    url(r'^video-del-comment/$', 'dilidili_dev.video_play.del_video_comment'),
    url(r'^video-set-collcetion/$', 'dilidili_dev.video_play.set_collection'),
    url(r'^video-set-like/$', 'dilidili_dev.video_play.set_like'),
    url(r'^video-add-money/$', 'dilidili_dev.video_play.add_money'),
    url(r'^home/', include([
        url(r'^$', 'dilidili_dev.views.home'),
        url(r'^following/$', 'dilidili_dev.home_view.following'),
        url(r'^follower/$', 'dilidili_dev.home_view.follower'),
        url(r'^collection/$', 'dilidili_dev.home_view.collection'),
        url(r'^center/$', 'dilidili_dev.home_view.center')
    ])),
    url(r'^upload/$', 'dilidili_dev.views.upload'),
    url(r'^upload-photo/$', 'dilidili_dev.upload_photo.upload_photo'),
    url(r'^upload-success/$', 'dilidili_dev.upload_photo.upload_success'),
    url(r'^process-photo/$', 'dilidili_dev.upload_photo.process_img', name='process-photo'),
    url(r'^search/$', 'dilidili_dev.search.search_mainpage'),
    url(r'^search/request/$', 'dilidili_dev.search.search'),
    url(r'^search/resulthtml/$', 'dilidili_dev.search.search_html'),
    url(r'^inbox/$', 'dilidili_dev.message.inbox'),
    url(r'^unread-msg/$', 'dilidili_dev.message.get_unread_num'),
    url(r'^sendto/(?P<user_id>[0-9]+)/$', 'dilidili_dev.message.sendto'),
    url(r'^del-msg/(?P<user_id>[0-9]+)/(?P<msg_id>[0-9]+)/$', 'dilidili_dev.message.del_msg'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
