from django.shortcuts import render
from .models import *
from django.template import loader
from django.http import HttpResponse

# Create your views here.

var=Cars.objects.filter(variant='Diesel')
def cars(request):
    return render(request,'base.html')

def cdetail(request,id):
    de=Cars.objects.get(id=id)
    return render(request,'det.html',{'de':de})

def diesel(request):
    var=Cars.objects.filter(variant='Diesel')
    return render(request,'diesel.html',{'var':var})

def petrol(request):
    var=Cars.objects.filter(variant='Petrol')
    return render(request,'petrol.html',{'var':var})
    
def electric(request):
    var=Cars.objects.filter(variant='Electric')
    return render(request,'electric.html',{'var':var})

def cng(request):
    var=Cars.objects.filter(variant='CNG')
    return render(request,'cng.html',{'var':var})


def tata(request):
    var=Cars.objects.filter(brand='TATA')
    return render(request,'tata.html',{'var':var})

def mg(request):
    var=Cars.objects.filter(brand='MG')
    return render(request,'mg.html',{'var':var})  

def mahindra(request):
    var=Cars.objects.filter(brand='Mahindra')
    return render(request,'mahindra.html',{'var':var})  

def maruti(request):
    var=Cars.objects.filter(brand='Maruti Suzuki')
    return render(request,'maruti.html',{'var':var})  

def hyundai(request):
    var=Cars.objects.filter(brand='Hyundai')
    return render(request,'hyundai.html',{'var':var})

def tataaltroz(request):
    var=Cars.objects.filter(name='TATA Altroz')
    return render(request,'tataaltroz.html',{'var':var})

def mghector(request):
    var=Cars.objects.filter(name='MG Hector')
    return render(request,'tataaltroz.html',{'var':var})


def mahindraxuv300(request):
    var=Cars.objects.filter(name='Mahindra XUV300')
    return render(request,'tataaltroz.html',{'var':var})


def marutisuzukiswiftldi(request):
    var=Cars.objects.filter(name='Maruti Suzuki Swift LDI')
    return render(request,'tataaltroz.html',{'var':var})


def hyundaivenue(request):
    var=Cars.objects.filter(name='Hyundai Venue')
    return render(request,'tataaltroz.html',{'var':var})





def tatanexon(request):
    var=Cars.objects.filter(name='TATA Nexon')
    return render(request,'tataaltroz.html',{'var':var})



def mgastor(request):
    var=Cars.objects.filter(name='MG Astor')
    return render(request,'tataaltroz.html',{'var':var})


def mahindrascorpion(request):
    var=Cars.objects.filter(name='Mahindra Scorpio N')
    return render(request,'tataaltroz.html',{'var':var})


def marutisuzukifronx(request):
    var=Cars.objects.filter(name='Maruti Suzuki Fronx')
    return render(request,'tataaltroz.html',{'var':var})


def hyundaii20nline(request):
    var=Cars.objects.filter(name='Hyundai i20 N Line')
    return render(request,'tataaltroz.html',{'var':var})


def tatatiagoev(request):
    var=Cars.objects.filter(name='TATA Tiago EV')
    return render(request,'tataaltroz.html',{'var':var})


def mgcometev(request):
    var=Cars.objects.filter(name='MG Comet EV')
    return render(request,'tataaltroz.html',{'var':var})


def mahindraxuv400(request):
    var=Cars.objects.filter(name='Mahindra XUV400')
    return render(request,'tataaltroz.html',{'var':var})


def marutigrandvitara(request):
    var=Cars.objects.filter(name='Maruti Grand Vitara')
    return render(request,'tataaltroz.html',{'var':var})


def hyundaikonaelectric(request):
    var=Cars.objects.filter(name='Hyundai Kona Electric')
    return render(request,'tataaltroz.html',{'var':var})


def tatatiago(request):
    var=Cars.objects.filter(name='TATA Tiago')
    return render(request,'tataaltroz.html',{'var':var})


def mgastorcng(request):
    var=Cars.objects.filter(name='MG Astor CNG')
    return render(request,'tataaltroz.html',{'var':var})


def mahindrakuv100nxttrip(request):
    var=Cars.objects.filter(name='Mahindra KUV100 NXT Trip')
    return render(request,'tataaltroz.html',{'var':var})


def marutisuzukispresso(request):
    var=Cars.objects.filter(name='Maruti Suzuki S-Presso')
    return render(request,'tataaltroz.html',{'var':var})


def hyundaigrandi10nios(request):
    var=Cars.objects.filter(name='Hyundai Grand i10 NIOS')
    return render(request,'tataaltroz.html',{'var':var})

  


def login(request):
    return render(request,'login.html') 


def register(request):
    return render(request,'register.html')  