from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404 
from .models import List, Bots, Queue, Proxies, Count

from django.views.decorators.csrf import csrf_exempt, csrf_protect

# from __future__ import division
from datetime import datetime, timedelta
import string

def totimestamp(dt, epoch=datetime(1970,1,1)):
    td = dt - epoch
    # return td.total_seconds()
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6 


import json
title = "Omlet Arcade Bot"
my_list=[ 
    {"title": "FREE TRIAL VIEW BOTS","url":"sites.views.freetrial","urls":"sites:freetrial","count":0,"used":0},
    {"title":"VIEW BOTS","url":"sites.views.shop","urls":"sites:shop","count":0,"used":0}
    ]
nav_list=[
    {"title": "FREE TRIAL", "urls": "sites:freetrial"},{"title":"SHOP","urls":"sites:shop"}
]

paypal_client_id="Acy2-a8xPnuhXCCNVWIucs4gE-sfstuo6s2QMOgHcJOKJAaw2xby0UhTsWLr2Tl4TUsxyXqe1H-C-z2z"
paypal_secret_id="ECYVwZ7GCoITw81qJFasaLU8xNfu4PhnIO1NRUJaqPi9HS_JITu3-M5rholwZMjAsypJOvgrlwVDrEEf"



def GetCount():
    # data = 0
    a=1
    b=2
    c=3
    d=5
    try:
        query = Count.objects.get(name='freetrial-visit')
        my_list[0]["count"] = query.count
        query = Count.objects.get(name='shop-visit')
        my_list[1]["count"] = query.count
    except Exception as e:
        print("ERROR: " + str(e))
        pass
    # return data


def home(request):
    GetCount()
    nav = "."
    isnav = ""
    site="home"
    # now = datetime.utcnow()
    # now=totimestamp(now)
    # article = List()
    # article.ft_follow = str(now)
    # article.ft_view = str(now)
    # article.ft_like = str(now)
    # article.save()
    
    # follow = List.objects.get(id=1).ft_follow
    # print(follow)
    return render(
        request, 
        'sites/home.html', 
        {
            'title':title, 
            'nav':nav, 
            'isnav': isnav,
            'my_list':my_list,
            'nav_list':nav_list
        }
    )

@csrf_exempt
def freetrial(request):
    GetCount()
    nav = "."
    isnav = ""
    site="freetrial"

    @csrf_protect
    def protected_path(request):
        pass
    if request.method=='POST':
        protected_path(request)

    return render(
        request, 
        'sites/freetrial.html', 
        {
            'title': title, 
            'nav': nav, 
            'isnav': isnav,
            'site': site,
            'my_list': my_list,
            'nav_list': nav_list
        }
    )

def shop(request):
    GetCount()
    nav = "."
    isnav = ""
    site="shop"
    if request.method=='POST':
        pass
    return render(request, 
    'sites/shop.html', 
    {'title':title, 
    'nav':nav, 
    'isnav': isnav,
    'site':site,
    'my_list':my_list,
    'nav_list':nav_list, 
    'paypal_client_id':paypal_client_id
    }
    )
def error(request):
    source = "."
    return render(request, 'sites/error.html', {'title':title, 'source':source})

def api(request):
    if request.method == 'GET':
        
        if request.GET.get('q')=="fgfz544wbw46b4wbb4":



            if request.GET.get('number'):
                if request.GET.get('number').isdigit():
                    number=int(request.GET.get('number'))
                    y = get_offline_bot(number)
                    return HttpResponse(y)
                
                elif request.GET.get('test')=='true':

                    # query = List.objects.get(id=2)
                    # query.follow=query.ft_follow
                    # query.like=query.ft_follow
                    # query.view=query.ft_follow
                    # query.save()
                    
                    query = List.objects.get(id=2)
                    data={
                        "freetrial_follow": query.ft_follow,
                        "freetrial_like": query.ft_like,
                        "freetrial_view": query.ft_view,
                        "follow": query.follow,
                        "like": query.like,
                        "view": query.view,
                    } 


                    y = json.dumps(data)

            
                    return HttpResponse(y)
    source = "."
    return render(request, 'sites/error.html', {'title':title, 'source':source})

def handler404(request, exception):
    return render(request, 'error.html', locals())


#### FUNCTIONS BEGIN
def get_offline_bot(number):
    status='NULL'
    query = Bots.objects.filter(name='NULL')
    if len(query)>0:
        for key, value in query.items():

            if 'name' in key:
                if query['kind'] == number:
                    status = value
                    break
    return status
#### FUNCTIONS END