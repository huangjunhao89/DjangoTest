# coding:utf-8
from django.http import *
from django.shortcuts import render,render_to_response
import os
from TestModel.models import Test

def hello(request):
    return HttpResponse('Hello World !')

def static_display1(request):
    p1 = {
        'name':'lily',
        'age':21,
    }
    p2 = {
        'name':'tom',
        'age':32,
    }

    # return render(request,'static_display1.html',{'name':'huangjunhao','age':28})
    return render(request, 'static_display1.html',p2)

def static_display2(request):
    return render_to_response('static_display2.html')

#表单
def search_form(request):
    return render_to_response('search_form.html')
#表单处理
def search_form_do(request):
    return HttpResponse("your name is "+request.GET['Name_html']+";"+"I'm "+request.GET['Age_html'])


#post视图和处理方式在同一函数
def search_post_do(request):
    dict1 = {}
    if request.POST :
        dict1['post_name'] = request.POST['name_html']
        dict1['post_age'] = request.POST['age_html']
        dict1['post_address'] = request.POST['address_html']
        dict1['post_date'] = request.POST['date_html']
        if dict1['post_name'] :
            db = Test(name=dict1['post_name'],age=dict1['post_age'],address=dict1['post_address'],data=dict1['post_date'])
            db.save()
    return  render(request,'post.html',dict1)

def base(request):
    return render_to_response("base.html")

def login(request):
    return render_to_response("login.html")