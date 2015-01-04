__author__ = 'utsav'

from crawlers import Course, CourseDetails
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        Course.objects.all().delete()
        CourseDetails.objects.all().delete()