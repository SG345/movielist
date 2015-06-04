from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(__package__ + '.views',
    url(r'^$', 'landing_page', {}, 'landing_page.html'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movies/$', 'movielist'),
    url(r'^movies/detail/(?P<movie_id>\d+)/$', 'getmovie'),
)
