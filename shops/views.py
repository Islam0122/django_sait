from django.shortcuts import render , HttpResponse
import datetime
# Create your views here.
a = datetime.datetime.now()

#1
def heloo_v(request):
    if request.method == 'GET':
        return HttpResponse(f"Hello! Its my project")
#2
def data_v(request):

    if request.method == 'GET':
        return HttpResponse(f"year : {a.year}\n"
                            f"day : {a.day}\n"
                            f"day of the week : {a.weekday() }\n"
                            f"time : -> hour {a.hour } : minute {a.minute}\n"
                            )
#3
def goodbye_v(request):
    if request.method == 'GET':
        a = datetime.datetime.now()

        if  a.hour == 22 or 23 or 00 or 1:
            return HttpResponse(f"sleep well \n"
                               f"user")
        elif a.hour == 6 or 7 or 8 or 9 :
            return HttpResponse(f"Goodbye morning!\n"
                                f"user")
        elif a.hour == 12 or 13  or 14 or 15:
            return HttpResponse(f"good day |!\n"
                                f"user")
        else:
            return HttpResponse(f"Goodbye user!\n"
                                f"")

