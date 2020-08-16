from django.shortcuts import render
from django.http import JsonResponse
from .models import user
from . import sendOTP, sendMail
import json
from random import randint

# Create your views here.

def doLogin(request):
    res = {}
    temp2 = {}
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            print(data['mobile'])
            print(data['password'])
            rec = user.objects.filter(mobile=data['mobile']).filter(password=data['password'])
            print(len(rec))
            if len(rec) > 0:
                temp2['loginStatus'] = 1
                temp = {}
                temp['name'] = rec[0].name
                temp['email'] = rec[0].email
                temp['mobile'] = rec[0].mobile
                temp2['user'] = temp

            else:
                temp2['loginStatus'] = -1

        res['status'] = 1
        res['data'] = temp2
    except Exception as e:
        print(e)
        res['status'] = 0
    return JsonResponse(res)

def doRegister(request):
    res = {}
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            if len(data['fname']) == 0 or len(data['lname']) == 0 or len(data['email']) == 0 or len(data['mobile']) == 0:
                res['status'] = -1
            else:
                check_rec1=user.objects.filter(email=data['email'])
                check_rec2 = user.objects.filter(mobile=data['mobile'])
                if len(check_rec1) > 0 or len(check_rec2) > 0:
                    res['status'] = -2
                else:
                    rec_n = user()
                    rec_n.name = data['fname']+ ' '+ data['lname']
                    rec_n.email = data['email']
                    rec_n.mobile = data['mobile']
                    rec_n.password= data['password']
                    rec_n.user_id = data['mobile']
                    rec_n.save()
                    # sendOTP.initMsg(rec_n.mobile, rec_n.password)
                    # sendMail.send_mail_digest(data['email'], data['fname'], 'Registration Successful', rec_n.password)
                    res['status'] = 1
    except Exception as e:
        print(e)
        res['status'] = 0
    return JsonResponse(res)

