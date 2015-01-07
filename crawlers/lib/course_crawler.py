__author__ = 'utsavnarayan'

from bs4 import BeautifulSoup
from crawlers import Course, CourseDetails
import urllib2
from collections import namedtuple


_BASE_URL = "https://www.open2study.com"
_COURSES_URL = _BASE_URL + '/courses/'


CourseInfo = namedtuple('CourseDetails',
                        ['short_url', 'name', 'instructor', 'summary', 'full_summary', 'syllabus', 'popularity'])


class InvalidUrlException(Exception):
    pass


class AlreadyCrawledUrl(Exception):
    pass


def _fetch_all_course_urls():
    course_urls = []
    soup = BeautifulSoup(urllib2.urlopen(_COURSES_URL))

    for link in soup.find_all('a'):
        if '/node/' in link.get('href'):
            course_urls.append(_BASE_URL + link.get('href'))

    return course_urls


def _fetch_course_info(course_url):
    """
    Contains the main logic of parsing the html soup and returning relevant data
    """
    if _BASE_URL not in course_url:
        raise InvalidUrlException

    crawled_urls = [x.url for x in Course.objects.all()]
    if course_url in crawled_urls:
        raise AlreadyCrawledUrl

    soup = BeautifulSoup(urllib2.urlopen(course_url))
    return CourseInfo(short_url=soup.find('article')['about'],
                      name=soup.find('h1').get_text(),
                      instructor=soup.find('h5').get_text(),
                      summary=soup.find('div', {"class": "summary"}).get_text(),
                      full_summary=soup.find('div', {"class": "full-body"}).get_text(),
                      syllabus=soup.find('div', {"class": "whatyouwilllearncontainer"}).get_text(),
                      popularity=int(soup.find('div', {"class": "student-numbers-header"}).get_text().split(' ')[0]))


def _save_course(url, short_url, name):
    """
    Save url, short url and name of course in 'Course' model
    """
    course = Course(url=url, short_url=short_url, name=name)
    course.save()
    return course


def _save_course_details(course, short_url, instructor, summary, full_summary, syllabus, popularity):
    """
    Save course (foreign key), short url, instructor, summary, full_summary, syllabus, popularity
    in 'CourseDetails' model
    """
    course_details = CourseDetails(course=course,
                                   short_url=short_url,
                                   instructor=instructor,
                                   summary=summary,
                                   full_summary=full_summary,
                                   syllabus=syllabus,
                                   popularity=popularity)
    course_details.save()


def crawl_course_urls(course_urls):
    """
    For crawling a specific course page for details
    """
    for course_url in set(course_urls):
        course_info = _fetch_course_info(course_url)

        course = _save_course(_BASE_URL+course_info.short_url,
                              course_info.short_url,
                              course_info.name)

        _save_course_details(course,
                             course_info.short_url,
                             course_info.instructor,
                             course_info.summary,
                             course_info.full_summary,
                             course_info.syllabus,
                             course_info.popularity)


def crawl_courses(course_urls):
    if course_urls:
        crawl_course_urls(course_urls.split(','))
    else:
        course_urls = _fetch_all_course_urls()
        crawl_course_urls(course_urls)