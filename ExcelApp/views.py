from django.shortcuts import render,get_object_or_404
from .models import CabDetails
from django import forms
from dataservice.xldata import get_xl_data
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


class UploadFileForm(forms.Form):
    file = forms.FileField()


class SearchForm(forms.Form):
    my_emp_id = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Your Employee ID', 'class':'form-control form-control-white', 'required':'True'}))


def HomePage(request):
    return render(request, 'ExcelApp/HomePage.html', {})


@login_required
def upload(request):    
    if request.method == "POST":
        me=User.objects.get(username='admin586')
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
        })


def search(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            empId=form.cleaned_data['my_emp_id']
            #cabdetails_obj=get_object_or_404(CabDetails.objects.filter(empId=empId))
            try:
                 instance = CabDetails.objects.get(empId=empId)
            except CabDetails.DoesNotExist:
                 return render(request,'ExcelApp/errPage.html')
           
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
