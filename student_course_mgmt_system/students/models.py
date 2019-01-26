# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from courses.models import Course

class Student(models.Model):
    name = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)
