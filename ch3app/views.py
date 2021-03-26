from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
def handle_uploaded_file(f,p):
    with open('{}/{}'.format(p,str(f)), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def file_uploads_p210(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if form.is_valid():
            path =  form.cleaned_data['path']
            for f in files:
                handle_uploaded_file(f,path)
            return HttpResponseRedirect('/ch3app/upload_success/')
    else:
        form = UploadFileForm()
        return render(request, 'ch3app/upload.html', {'form': form})
def upload_success(request):
    return HttpResponse('upload is completed')





