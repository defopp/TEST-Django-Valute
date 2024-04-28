from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework.renderers import JSONRenderer

from .serializers import CoinSerializer
from .models import Coin

# Create your views here.
class MainView(View):
    def get(self, request):
        return HttpResponse('MainView')
        
class RateView(View):
    def get(self, request):
        
        if len(request.GET) != 0:
            if request.GET["charcode"] and request.GET["date"]:
                
                try: 
                    valute_qs = Coin.objects.all().values('charcode','date','rate').filter(charcode=request.GET["charcode"], date=request.GET["date"]).order_by("-id")[0]
                    serializer = CoinSerializer(valute_qs)
                    return HttpResponse(JSONRenderer().render(serializer.data))

                except: return HttpResponse('None')
                    
            else: return HttpResponse('RateView')
        else: return HttpResponse('RateView')

    