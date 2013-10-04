from django.conf.urls import patterns, include, url
from codecamp import views

# for admin page
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^polls/(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^polls/(?P<question_id>\d+)/results/$', views.results, name='results'),
    url(r'^polls/(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^admin/', include(admin.site.urls)),
)
