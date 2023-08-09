from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from . forms import companyForm,EmployeeForm,DeviceForm,TrackingForm
from . models import Company,Employee,Device,Tracking
# from django.contrib import messages
# Create your views here.
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