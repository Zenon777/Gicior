from django.conf.urls.defaults import patterns, include, url
from mysite.blog.views import archive

urlpatterns = patterns('',
    url(r'^blog/', include('mysite.blog.urls')),
)

urlpatterns = patterns('',
	url(r'^$', archive),
)