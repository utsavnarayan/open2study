from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)


# Views for user:
# homepage or localhost:port will show a list of all crawled urls
# homepage/course/course-name will show details of a specific course
urlpatterns += patterns('',
    url(r'^$', views.index),
    url(r'^courses/(?P<course_name>((\w+)(-(\w+))*))', views.course),
    url(r'^crawl/', views.crawl_urls),
    url(r'^delete/', views.delete_all_courses),
)

handler404 = views.show_error_404
handler500 = views.show_error_500
