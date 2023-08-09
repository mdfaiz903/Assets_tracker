from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from . forms import companyForm,EmployeeForm,DeviceForm,TrackingForm
from . models import Company,Employee,Device,Tracking
# from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, TrackingSerializer
from rest_framework import generics
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, TrackingSerializer
# Create your views here.

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class TrackingList(generics.ListCreateAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer

class TrackingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tracking.objects.all()
    serializer_class = TrackingSerializer

@api_view(['GET'])
def api_company_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_device_list(request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_tracking_list(request):
    tracking_records = Tracking.objects.all()
    serializer = TrackingSerializer(tracking_records, many=True)
    return Response(serializer.data)
def homeview(request):
    dataset = Tracking.objects.all()
    
    return render(request,'common_code/base.html',{'dataset':dataset})
def company_view(request):
    if request.method=='POST':
        c_frm = companyForm(request.POST)
        name = request.POST['Name']
        location = request.POST['Location']
        obj = Company(c_name=name,c_location=location)
        obj.save()
        return HttpResponseRedirect("/Myapp")
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
            return HttpResponseRedirect("/Myapp")
    else:
        e_frm = EmployeeForm()    
    return render(request,'Assets_tracker/employee.html',{'form':e_frm})

def device_view(request):
    if request.method=='POST':
        frm = DeviceForm(request.POST)
        if frm.is_valid():
            obj=frm.save()
            return HttpResponseRedirect("/Myapp")
    else:
        frm = DeviceForm()
    return render(request,'Assets_tracker/device.html',{'form':frm})        

def tracking_view(request):
    if request.method=='POST':
        frm =   TrackingForm(request.POST)
        if frm.is_valid():
            obj= frm.save()
            return HttpResponseRedirect("/Myapp")

    else:
        frm = TrackingForm()
        
    return render(request,'Assets_tracker/tracking.html',{'form':frm})  


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    # context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Tracking, id = id)
 
    # pass the object as instance in form
    form = TrackingForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/Myapp")
 
    # add form dictionary to context
    context ={"form":form}
 
    return render(request, "Assets_tracker/updateview.html", context)