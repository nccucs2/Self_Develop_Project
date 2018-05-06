from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
def login(request):
    template = get_template('login.html')

    if request.user.is_authenticated:
        return HttpResponseRedirect('/student/')
    try:
        username = request.GET['usr_id']
        password = request.GET['usr_pass']
        user = auth.authenticate(username=username, password=password)
    except:
        user_id = None
        user_password = None
        user = None
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/student/')
    else:
        html = template.render(locals())
        return HttpResponse(html)

        #return render_to_response('login.html')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/student/')

def student(request):
    template = get_template('student.html')
    html = template.render(locals())
    return HttpResponse(html)
# Create your views here.
