from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.home', name='home'),
    url(r'^how-it-works/$', 'core.views.how_it_works', name='how_it_works'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('profiles.urls', namespace='profiles')),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^issues/', include('issues.urls', namespace='issues')),
    url(r'^hackathons/', include('hackathons.urls', namespace='hackathons')),
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
