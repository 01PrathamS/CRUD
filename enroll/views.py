from http.client import HTTPResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration 
from .models import User 
from django.views.generic.base import TemplateView,RedirectView
from django.views import View 


######################## Class Based Views #############################################

## to add User and show its detail on the same page
class UserAddShowView(TemplateView):
    # directly render to this template
    template_name = 'enroll/addandshow.html'

    ## if user sends get request
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {'stu':stud, 'form':fm}
        return context
    #if user sends post request
    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
        return HttpResponseRedirect('/')

## we can delete the data and redirect to main page
class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


# to update users detail its showing on the other page..
class UserUpdateview(View):

    # first user sends get request
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'enroll/updatestudent.html',{'form':fm})
    #when enduser update the data then it goes post request then on this request goes on.
    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')




#######################Function Based Views###################################



## to add userd data
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
        fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm, 'stu':stud})


# to update user data 
def update_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html',{'form':fm})

## to delete user data
def deletedata(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')