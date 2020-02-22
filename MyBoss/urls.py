from django.conf.urls import url

from MyBoss import views

app_name='MyBoss'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^liepin/$', views.liepin, name='liepin'),
    url(r'^local_bj/$', views.local_bj, name='local_bj'),
    url(r'^local_sh/$', views.local_sh, name='local_sh'),
    url(r'^local_gz/$', views.local_gz, name='local_gz'),
    url(r'^local_sz/$', views.local_sz, name='local_sz'),
    url(r'^condition_bx/$', views.condition_bx, name='condition_bx'),
    url(r'^condition_dz/$', views.condition_dz, name='condition_dz'),
    url(r'^condition_bk/$', views.condition_bk, name='condition_bk'),
    url(r'^condition_ss/$', views.condition_ss, name='condition_ss'),
    url(r'^liepin_overseas/$', views.liepin_overseas, name='liepin_overseas'),
    url(r'^company_detail/$', views.company_detail, name='company_detail'),
    url(r'^liepin_community/$', views.liepin_community, name='liepin_community'),
    url(r'^test/$', views.test, name='test'),
    url(r'^test2/$', views.test2, name='test2'),

]
