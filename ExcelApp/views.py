from django.shortcuts import render
from .models import CabDetails
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()


def HomePage(request):
    return render(request, 'ExcelApp/HomePage.html', {})


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            #return excel.make_response(filehandle.get_sheet(), "csv",
            #                          file_name="download")
			#Need to develop the function call
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

