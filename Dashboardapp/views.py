from django.shortcuts import HttpResponse, render
import openpyxl
import pandas as pd
from .add_data import Command
from Dashboardapp.models import  VC_Master
from Dashboardapp.models import  V_master
from Dashboardapp.models import  StrLoc
from Dashboardapp.models import MAP 
from Dashboardapp.models import Part_Master
from Dashboardapp.models import MRP
from Dashboardapp.models import DMLdetails

 
from django.template import loader

def AdminPage(request):
    return render(request,'example.html')

def VCpage(request):
    if request.method == 'POST':
        excel = request.FILES.get('myfile').read()
        Command.VC_master(excel)
    VCm = VC_Master.objects.all()
    print(VCm)
    col = [x.name for x in VC_Master._meta.get_fields()]
    template = loader.get_template('VCMASTER.html')
    print(template)
    context = {
        'Vcno' : VCm,
        'col' : col,
    }
    return HttpResponse(template.render(context, request))

def Vpage(request):
    if request.method == 'POST':
        excel = request.FILES.get('myfile').read()
        Command.V_master(excel)
    Vm = V_master.objects.all()
    print(Vm)
    col = [x.name for x in VC_Master._meta.get_fields()]
    template = loader.get_template('VMASTER.html')
    print(template)
    context = {
        'Vno' : Vm,
        'col' : col,
    }
    return HttpResponse(template.render(context, request))
     
     
    


    
   
     

def Partpage(request):
    if request.method == 'POST':
        excel = request.FILES.get('myfile').read()
        Command.Part_Master(excel)
    PM = Part_Master.objects.all()
    print(PM)
    col = [x.name for x in Part_Master._meta.get_fields()]
    template = loader.get_template('PARTMASTER.html')
    print(template)
    context = {
        'Pno' : PM,
        'col' : col,
    }
    return HttpResponse(template.render(context, request))
    

    

def StrPage(request):
    if request.method == 'POST':
        excel = request.FILES.get('myfile').read()
        Command.StrLoc(excel)
    SL = StrLoc.objects.all()
    print(SL)
    col = [x.name for x in StrLoc._meta.get_fields()]
    template = loader.get_template('STRLOC.html')
    print(template)
    context = {
        'Sno' : SL,
        'col' : col,
    }
    return HttpResponse(template.render(context, request))
    

def MapPage(request):
    if request.method == 'POST':
        excel = request.FILES.get('myfile').read()
        Command.MAP(excel)
    MP = MAP.objects.all()
    print(MP)
    col = [x.name for x in MAP._meta.get_fields()]
    template = loader.get_template('MAPMASTER.html')
    print(template)
    context = {
        'Mno' : MP,
        'col' : col,
    }
    return HttpResponse(template.render(context, request))
   
    
def mrpPage(request):
    if request.method == 'POST':
        excel = request.FILES.get('myfile').read()
        Command.MRP(excel)
    MR = MRP.objects.all()
    print(MR)
    col = [x.name for x in MRP._meta.get_fields()]
    template = loader.get_template('MRP.html')
    print(template)
    context = {
        'Mrn' : MR,
        'col' : col,
    }
    return HttpResponse(template.render(context, request))



def dmlPage(request):
    if request.method == 'POST':
        excel = request.FILES.get('myfile').read()
        Command.DMLdetails(excel)
    DL = DMLdetails.objects.all()
    print(DL)
    col = [x.name for x in DMLdetails._meta.get_fields()]
    template = loader.get_template('DML.html')
    print(template)
    context = {
        'DLn' : DL,
        'col' :col,
    }
    return HttpResponse(template.render(context,request))