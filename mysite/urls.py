from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views
from blog.views import archive

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'polls.views.index'),
    url(r'^polls/$', 'polls.views.index2'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    url(r'^blog/', 'blog.views.archive'),
)


urlpatterns += patterns('',
	url(r'^admin/', include(admin.site.urls)),
)

