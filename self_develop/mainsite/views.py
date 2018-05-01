from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
def login(request):
    template = get_template('login.html')
    html = template.render(locals())
    return HttpResponse(html)
def student(request):
    template = get_template('student.html')
    html = template.render(locals())
    return HttpResponse(html)
# Create your views here.
