from django import forms
from . models import Employee,Device,Tracking



class companyForm (forms.Form):
    Name = forms.CharField(label="Company Name")
    Location = forms.CharField(label='Company Location')

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'


class TrackingForm(forms.ModelForm):
    class Meta:
        model = Tracking
        fields = '__all__'