# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Course(models.Model):
    title = models.TextField()
