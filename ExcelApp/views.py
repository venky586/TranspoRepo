from django.shortcuts import render,get_object_or_404
from .models import CabDetails
from django import forms
from dataservice.xldata import get_xl_data
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect


class UploadFileForm(forms.Form):
    file = forms.FileField()


class SearchForm(forms.Form):
    my_emp_id = forms.CharField()


def HomePage(request):
    return render(request, 'ExcelApp/HomePage.html', {})


def upload(request):
    me=User.objects.get(username='admin')
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            data_dict=get_xl_data(filehandle)
            keys=data_dict.keys()
            for eachKey in keys:
                dataList=data_dict.get(eachKey)
                sNo=dataList[0]
                cNo=dataList[1]
                CabDetails.objects.create(
                    author=me,
                    empId=eachKey,
                    cabNo=cNo,
                    cabSerialNo =sNo,
                    publishDate =timezone.now())
            return render(
                request,
                'ExcelApp/SuccessPage.html',
                {})
    else:
        form = UploadFileForm()
    return render(
        request,
        'ExcelApp/upload_form.html',
        {
            'form': form,
            'title': 'Cab details upload',
            'header': ('Please upload cab details file : ')
        })


def search(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            empId=form.cleaned_data['my_emp_id']
            cabdetails_obj=get_object_or_404(CabDetails.objects.filter(empId=empId))
            print(cabdetails_obj.cabSerialNo)
            print(cabdetails_obj.empId)
            print(cabdetails_obj.cabNo)

            return render(
                    request,
                    'ExcelApp/resultsPage.html',
                    {'searchResults': cabdetails_obj,})
    else:
        form = SearchForm() # An unbound form

    return render(
        request,
        'ExcelApp/searchPage.html',
        {'form': form})
