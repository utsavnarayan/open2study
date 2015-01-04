__author__ = 'utsav'

from crawlers import crawl_courses
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        crawl_courses()