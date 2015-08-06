from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'dilidili_dev.views.personal'),
    url(r'^togglefollow/$', 'dilidili_dev.views.user_toggle_follow'),
    url(r'^admin/', include([
        url(r'^toggleupload/$', 'dilidili_dev.admin_views.toggle_user_upload'),
        url(r'^togglecomment/$', 'dilidili_dev.admin_views.toggle_user_comment'),
        url(r'^togglebullet/$', 'dilidili_dev.admin_views.toggle_user_bullet'),
    ])),
]
