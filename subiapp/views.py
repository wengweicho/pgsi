from django.shortcuts import render, redirect
from django.http import HttpResponse
from pathlib import Path
from sqlalchemy import create_engine
from subiapp.models import subiinfo
import pandas as pd
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def admissions(request):

    return render(request,"subiapp/admissions.html",locals())
#  taiwan1 新北市_區
def taiwan_map(request,var1=''):
    source = 'jsons/taiwan1_geo.json'
    show = 'true'
    if var1.find('刪') != -1:
        try:
            subiinfo.objects.get(name=var1.replace('刪','')).delete()
        except ObjectDoesNotExist:
            pass
    elif var1.find('修') != -1:
        modify_onerecord = subiinfo.objects.get(name=var1.replace('修',''))
        modify_onerecord.district=request.GET['district']
        modify_onerecord.name=request.GET['name']
        modify_onerecord.tel=request.GET['tel']
        modify_onerecord.addr=request.GET['addr']
        modify_onerecord.save()
    subiinfos = subiinfo.objects.filter(city=var1)
    #subiinfos = subiinfo.objects.all().order_by('district')
    return render(request,"subiapp/taiwan_map.html",locals())
def trust(request):
    return render(request,"subiapp/trust.html",locals())
def subiinfo_uploadfile(request,district=''):
    BASE_DIR = Path(__file__).resolve().parent.parent
    engine = create_engine('sqlite:///{}/db.sqlite3'.format(BASE_DIR))
    xlsxfile = str(BASE_DIR)+('/static/csv/')+ "amc.csv"
    df = pd.read_csv(xlsxfile)
    table_name = "subiapp_subiinfo"
    df.to_sql(table_name,con=engine, if_exists='replace',index_label='id',)
    message = '我完成了將所選的日報資料倒入資料庫,接下來繼續完成資料庫查詢'
    subiinfos = subiinfo.objects.all().order_by('district')
    return render(request,"subiapp/taiwan_map.html",locals())
def delete_onerecord(request,subi_name=''):
    try:
        onerecord_get_by_name = subiinfo.objects.get(name=subi_name)
        return render(request, "subiapp/delete_onerecord.html", locals())
    except:
        return render(request,"subiapp/login.html",locals())
def modify_onerecord(request,subi_name=''):
    try:
        onerecord_get_by_name = subiinfo.objects.get(name=subi_name)
        return render(request, "subiapp/modify_confirm.html", locals())
    except:
        request.session["action_flag"] = 'modify'
        return render(request,"subiapp/login.html",locals())
def login(request,subi_name=''):  #登入
	messages = ''  #初始時清除訊息
	if request.method == 'POST':  #如果是以POST方式才處理
		name = request.POST['username'].strip()  #取得輸入帳號
		password = request.POST['passwd']  #取得輸入密碼
		user1 = authenticate(username=name, password=password)  #驗證
		if user1 is not None:  #驗證通過
			if user1.is_active:  #帳號有效
				auth.login(request, user1)  #登入
				request.session["username_forlogin"] = name
				onerecord_get_by_name = subiinfo.objects.get(name=subi_name)
				if request.session["action_flag"] == 'delete':
				    return render(request, "subiapp/delete_onerecord.html", locals())
				elif request.session["action_flag"] == 'modify':
				    return render(request, "subiapp/modify_confirm.html", locals())
			else:  #帳號無效z
				message = '帳號尚未啟用！'
		else:  #驗證未通過
			message = '登入失敗！'
	return render(request, "subiapp/login.html", locals())