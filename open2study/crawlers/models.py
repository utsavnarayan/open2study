from django.db import models

# Create your models here.


class Course(models.Model):
    url = models.URLField()
    short_url = models.TextField()
    name = models.TextField()

    def __unicode__(self):
        return self.name


class CourseDetails(models.Model):
    course = models.ForeignKey(Course)
    short_url = models.TextField()
    instructor = models.TextField()
    summary = models.TextField()
    full_summary = models.TextField()
    syllabus = models.TextField()
    popularity = models.IntegerField(default=0)

    def __unicode__(self):
        return self.course.name