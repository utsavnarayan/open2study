__author__ = 'utsav'

from django.http import HttpResponse
from django.template import loader,  RequestContext
from django.http import Http404

from crawlers.models import Course, CourseDetails
from crawlers import crawl_courses, InvalidUrlException
import json


def _show_error(request, error_code):
    template = loader.get_template("error.html")
    context = RequestContext(request, {
        'error_code': error_code,
    })
    return HttpResponse(template.render(context))


def show_error_404(request):
    return _show_error(request, 404)


def show_error_500(request):
    return _show_error(request, 500)


# Shows list of all crawled urls
def index(request):
    courses = Course.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'courses': courses,
    })
    return HttpResponse(template.render(context))


# Shows details of a course
def course(request, course_name):
    course_url = '/courses/' + course_name
    try:
        course_details = CourseDetails.objects.get(short_url=course_url)
    except CourseDetails.DoesNotExist:
        raise Http404

    template = loader.get_template('course_details.html')
    context = RequestContext(request, {
        'course_details': course_details,
    })
    return HttpResponse(template.render(context))


def crawl_urls(request):
    urls = request.REQUEST['urls']
    try:
        crawl_courses(urls)
        message = "Successfully crawled."
    except InvalidUrlException:
        message = "Crawl failed due to incorrect url."
    payload = {'message': message}
    return HttpResponse(json.dumps(payload), content_type='application/json')


def delete_all_courses(request):
    Course.objects.all().delete()
    CourseDetails.objects.all().delete()
    payload = {'message': "All courses successfully deleted."}
    return HttpResponse(json.dumps(payload), content_type='application/json')