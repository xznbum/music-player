from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opris.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


)

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'musicplayer.views.index', name="home"),
    url("^music", include("audiotracks.urls")),
    url("^(?P<username>[\w\._-]+)/music", include("audiotracks.urls")),
    url(r'^login$', 'django.contrib.auth.views.login', name="login"),
    url(r'^logout$', 'django.contrib.auth.views.logout', name="logout"),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),)
    urlpatterns += staticfiles_urlpatterns()
