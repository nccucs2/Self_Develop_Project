from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
def login(request):
    #template = get_template('login.html')
    if request.user.is_authenticated:
        return HttpResponseRedirect('/student/')
    try:
        username = request.POST['usr_id']
        password = request.POST['usr_pass']
        user = auth.authenticate(username=username, password=password)
    except:
        user = None

        #user_id = None
        #user_password = None


    if user is not None:
        if user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect('/student/')
    else:
        if request.POST:
            messages.error(request,'帳號或密碼錯誤')
        return render(request,'login.html',)

        """
        messages.error(request,'username or password not correct')
        return HttpResponseRedirect('/login/')
        html = template.render(locals())
        return HttpResponse(html)
        """


        #return render_to_response('login.html')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/student/')

def student(request):
    return render(request,'student.html')
    """
    template = get_template('student.html')
    html = template.render(locals())
    return HttpResponse(html)
    """
def grade(request):
    return render(request,'grade.html')

def gpa(request):
    return render(request,'gpa.html')

def course(request):
    return render(request,'course.html')

def suggest_course(request):
    return render(request,'suggest_course.html')
# Create your views here.
