# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
import time

#响应
def db(request):
    return HttpResponse("Hello, django!")
#重定向
def rebaidu(request):
    return redirect('http://www.baidu.com')
#替换
def index(request):
    now_time = time.strftime('%Y-%m-%d %X', time.localtime())
    return render(request, 'h1.html', {'now_time':now_time})