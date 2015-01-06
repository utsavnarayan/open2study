from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'open2study.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^$', views.index),
    url(r'^courses/(?P<course_name>((\w+)(-(\w+))*))', views.course),
)

handler404 = views.show_error_404
handler500 = views.show_error_500
