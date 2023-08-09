from django.shortcuts import render
from . forms import companyForm,EmployeeForm,DeviceForm,TrackingForm
from . models import Company,Employee,Device,Tracking
# Create your views here.
def homeview(request):
    context = {}
    context['dataset']= Tracking.objects.all()
    return render(request,'common_code/base.html',context)
def company_view(request):
    if request.method=='POST':
        c_frm = companyForm(request.POST)
        name = request.POST['Name']
        location = request.POST['Location']
        obj = Company(c_name=name,c_location=location)
        obj.save()
    else:
        c_frm= companyForm()
    return render(request,'Assets_tracker/company.html',{'form':c_frm})

def employee_view(request):
    if request.method=='POST':
        e_frm = EmployeeForm(request.POST)
        if e_frm.is_valid():
            e_id = e_frm.cleaned_data['e_id']
            e_name = e_frm.cleaned_data['e_name']
            e_email = e_frm.cleaned_data['e_email']
            company = e_frm.cleaned_data['company']
            obj = Employee(e_id=e_id,e_name=e_name,e_email=e_email,company=company)
            obj.save()
    else:
        e_frm = EmployeeForm()    
    return render(request,'Assets_tracker/employee.html',{'form':e_frm})

def device_view(request):
    if request.method=='POST':
        frm = DeviceForm(request.POST)
        if frm.is_valid():
            obj=frm.save()
    else:
        frm = DeviceForm()
    return render(request,'Assets_tracker/device.html',{'form':frm})        

def tracking_view(request):
    if request.method=='POST':
        frm =   TrackingForm(request.POST)
        if frm.is_valid():
            obj= frm.save()


    else:
        frm = TrackingForm()
        
    return render(request,'Assets_tracker/tracking.html',{'form':frm})  

# def list_view(request):
#     context = {}
#     context['dataset']= Tracking.objects.all()
#     return render(request,'common_code/base.html',context)