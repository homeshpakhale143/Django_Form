from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def college(request):
    ECO=CollegeForm()
    d={'ECO':ECO}
    if request.method=='POST':
        CFDO=CollegeForm(request.POST)
        if CFDO.is_valid():
            print(CFDO.cleaned_data)
            return HttpResponse('Data is Submitted')
        else:
            return HttpResponse('Data is Invalid')

    return render(request,'college.html',d)


