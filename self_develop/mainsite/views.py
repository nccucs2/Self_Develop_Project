from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
def login(request):
    template = get_template('login.html')
    user_id = "123"
    user_password = "345"
    try:
        user_id = request.GET['usr_id']
        user_password = request.GET['usr_pass']
        #print(user_id)
        #print(user_password)
    except:
        user_id = None
        user_password = None
    #print(user_id)
    #print(user_password)
    html = template.render(locals())
    return HttpResponse(html)

def student(request):
    template = get_template('student.html')
    html = template.render(locals())
    return HttpResponse(html)
# Create your views here.
