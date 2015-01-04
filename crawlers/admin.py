from django.contrib import admin
from crawlers.models import Course, CourseDetails


class CourseAdmin(admin.ModelAdmin):
    list_display = ('url', 'name')


class CourseDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructor', 'summary')


admin.site.register(Course)
admin.site.register(CourseDetails)
