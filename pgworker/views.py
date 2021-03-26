from django.shortcuts import render, redirect, HttpResponse
from bs4 import BeautifulSoup
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from pathlib import Path
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import Profile
from .forms import FilesUpload
from .models import UploadFiles
import shutil,os,re,json
BASE_DIR = Path(__file__).resolve().parent.parent

def copy_afile(file,dest_path):
    with open(dest_path, 'wb+')  as destination:     # 打开存储文件
        for chunk in file.chunks():          # 分块写入文件
            destination.write(chunk)
def one_level(folder_path):
    try:
        os.makedirs(folder_path)
    except OSError as e:
        if e.errno == 17:
            pass
def folder_copy(key,str_var):
    to_server_folder = os.path.join(BASE_DIR,"dictory_upload")
    folder_path=""
    while str_var.find('/') != -1:
        folder_path = folder_path+"/"+str_var[0:str_var.find('/')]
        one_level(to_server_folder+folder_path)
        str_var = str_var[str_var.find('/')+1:]

def upload(request):
    if request.method == 'GET':
        return render(request, 'upload_files.html')
    elif request.method == 'POST':
        dirlist = request.FILES.getlist("file_field", None)        #获取文件列表
        dict_file_path_pairs = json.loads(request.POST.get('directories', False))
        if not dirlist:
            return HttpResponse("没有上传内容")
        else:
            keys  = list(dict_file_path_pairs)
            index = -1
            for key in keys:
                index = index + 1
                folder_copy(dict_file_path_pairs.get(key),key)
                copy_afile(dirlist[index],os.path.join(BASE_DIR,"dictory_upload",key))
            return render(request, 'upload_files.html',locals())
    else:
            return HttpResponseRedirect("不支持的请求方法")

def handle_uploaded_folder(folder_source,path):
    shutil.copytree(folder_source, path)
def upload_files_temp(request):
    if request.method == "POST":
    # if the post request has a file under the input name 'document', then save the file.
        request_file = request.FILES['document'] if 'document' in request.FILES else None
        if request_file:
                # save attatched file

            # create a new instance of FileSystemStorage
            fs = FileSystemStorage()
            file = fs.save(request_file.name, request_file)
            # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
            fileurl = fs.path(file)
    return render(request, 'upload_files.html', locals())


def handle_uploaded_file_ok0205(f,p):
    with open('{}/{}'.format(p,str(f)), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def handle_uploaded_file(f,p):
    with open('{}/{}'.format(p,str(f)), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def upload_files(request):
    if request.method == "POST":
        form = FilesUpload(request.POST, request.FILES)
        files = request.FILES.getlist('upload_files')
        if form.is_valid():
            path =  form.cleaned_data['upload_to']
            for f in files:
                handle_uploaded_file(f,path)

                #file_instance = UploadFiles(upload_files=f)
                #file_instance.save()
        #return redirect('upload_keyword')
    else:
        form = FilesUpload()
    return render(request, 'upload_files.html', locals())


def saveProfile(request):
    saved = False
    if request.method == "POST":
      #Get the posted form
        MyProfileForm = ProfileForm(request.POST, request.FILES)
        if MyProfileForm.is_valid():
            profile = Profile(picture=request.FILES['file'])
            profile.save()
            saved = True
    else:
        MyProfileForm = ProfileForm()
    return render(request, 'saved.html', locals())
def board(request):
    return redirect('/boardapp/index/')
def index(request):
    return render(request,"pgworker/index.html",locals())
def amc_index(request):
    return render(request,"pgworker/amc_index.html",locals())
def amc_carrer_plan(request):
    return render(request,"pgworker/amc_carrer_plan.html",locals())
def amc_happy_job(request):
    return render(request,"pgworker/amc_happy_job.html",locals())
def python_anywhere(request):
    return render(request,"pgworker/python_anywhere.html",locals())
def git_hub(request):
    return render(request,"pgworker/git_hub.html",locals())
def django_fw(request):
    return render(request,"pgworker/amc_happy_job.html",locals())
def bootstrap_fw(request):
    return render(request,"pgworker/bootstrap_fw.html",locals())
def data_view(request):
    return render(request,"pgworker/data_view.html",locals())
def data_reptile(request):
    return render(request,"pgworker/data_reptile.html",locals())
def data_reptile_lessson1(request):
    return render(request,"pgworker/data_reptile/data_reptile_lessson1.html",locals())
def data_reptile_lessson2(request):
    return render(request,"pgworker/data_reptile/data_reptile_lessson2.html",locals())
def data_reptile_lessson3(request):
#r = requests.get('https://www.1111.com.tw/search/job?ks=python&c0=100100%2C100200&gr=2&fs=1&page=1')
#r = requests.get('https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000%2C6001002000&edu=2&order=12&asc=0&page=1&mode=s&jobsource=2018indexpoc')
    list = []
    with open(str(BASE_DIR)+"/static/files/python_高中職_台北市_新北市_104.html") as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    jobs = soup.findAll('article')
    for job in jobs:
        if  job.get('data-cust-name') is not None:
            list.append(job.get('data-cust-name'))
            list.append(job.get('data-job-name'))
    skills = soup.findAll('p',class_="job-list-item__info b-clearfix b-content")
    insert_index = -1
    for skill in skills:
        skill_contents = skill.contents
        if skill_contents is not None:
            skill_contents_string = ' '.join([str(elem) for elem in skill_contents])
            skill_contents_string = re.sub("(?i)<.{0,1}em[^>]*>", "",skill_contents_string)
            insert_index = insert_index + 3
            list.insert(insert_index, skill_contents_string)
    list_lenth = int(len(list)/3)
    html_string='''<table class="table" style="width:100%">
                <thead>
                  <tr>
                    <th>公司</th>
                    <th>職稱</th>
                    <th>工作內容</th>
                  </tr>
                </thead>
                <tbody>
                {% for i in 0|range:list_lenth %}
                  <tr>
                    <td>{{list|index:i }}</td>
                    <td>{{list|index_plus_1:i }}</td>
                    <td>{{list|index_plus_2:i}}</td>
                  </tr>
                {% endfor %}
                </tbody>
                </table>'''
    return render(request,"pgworker/data_reptile/data_reptile_lessson3.html",locals())
def data_reptile_lessson4(request):
    return render(request,"pgworker/data_reptile/data_reptile_lessson4.html",locals())
def data_reptile_lessson5(request):
    return render(request,"pgworker/data_reptile/data_reptile_lessson5.html",locals())
def data_reptile_lessson6(request):
    return render(request,"pgworker/data_reptile/data_reptile_lessson6.html",locals())
