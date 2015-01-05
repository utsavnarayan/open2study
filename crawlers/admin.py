from django.contrib import admin
from crawlers.models import Course, CourseDetails


class CourseAdmin(admin.ModelAdmin):
    list_display = ('url', 'name')


class CourseDetailsAdmin(admin.ModelAdmin):
    list_display = ('course', 'instructor', 'summary')


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseDetails, CourseDetailsAdmin)
