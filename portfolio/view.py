from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import FileResponse
import os
from django.core.mail import send_mail
import requests


def Home(request):
    return render(request,'Home.html')
def sendmail(request):
    if request.method=='POST':
        email=request.POST.get("email")
        send_mail(
            'testing mail',
            'hiiii this is test msg',
            'dk1264428@gmail.com',
            [email],
            fail_silently=False
        )
        return HttpResponse("mail has sent")
    else:
        return HttpResponse("mail not sent")

def pdf_view(request):
        filepath = os.path.join('static', 'Deveshresume.pdf')
