__author__ = 'utsav'

from django.http import HttpResponse, Http404
from crawlers.models import Course, CourseDetails
from django.template import loader,  RequestContext
from django.http import Http404


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
