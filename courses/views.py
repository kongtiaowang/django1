# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from courses.models import Course

# Create your views here.
def abc(request):
	courses = Course.objects.all()
	output = ','.join([str(course) for course in courses])
	return HttpResponse(output)