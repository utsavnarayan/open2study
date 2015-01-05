__author__ = 'utsav'

from django.http import HttpResponse
from crawlers.models import Course, CourseDetails
from django.template import loader, Context, RequestContext


def index(request):
    courses = Course.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'courses': courses,
    })
    return HttpResponse(template.render(context))


def course(request, course_name):
    course_url = '/courses/' + course_name
    try:
        course_details = CourseDetails.objects.get(short_url=course_url)
    except CourseDetails.DoesNotExist:
        return show_404()

    template = loader.get_template('course_details.html')
    context = RequestContext(request, {
        'course_details': course_details,
    })
    return HttpResponse(template.render(context))


def show_404():
    template = loader.get_template("404.html")
    return HttpResponse(template.render(Context()))