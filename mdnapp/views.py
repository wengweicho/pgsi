from django.shortcuts import render

def index(request):  #刪除資料
	return render(request, "mdnapp/today.html", locals())
def pmv1(request):  #刪除資料
	return render(request, "mdnapp/pmv1.html", locals())
def pmv2(request):  #刪除資料
	return render(request, "mdnapp/pmv2.html", locals())
def pmv3(request):  #刪除資料
	return render(request, "mdnapp/pmv3.html", locals())



