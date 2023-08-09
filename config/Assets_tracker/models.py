from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    c_name = models.CharField(max_length=255)
    c_location = models.CharField(max_length=255)

    def __str__(self):
        return self.c_name
    


class Employee(models.Model):
    e_id = models.IntegerField()
    e_name = models.CharField(max_length=255)
    e_email = models.EmailField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.e_name

class Device(models.Model):
    DEVICE_TYPE = (
        ('Phone','Phone'),
        ('Tablet','Tablet'),
        ('Laptop','Laptop'),
        ('Other','Other'),
    )
    type = models.CharField(max_length=50,choices=DEVICE_TYPE)
    
    serial_number = models.CharField(max_length=100)
    device_condition = models.TextField()
    def __str__(self):
        return f"{self.type}-{self.serial_number}"

class Tracking(models.Model):
    device = models.ForeignKey(Device,on_delete=models.CASCADE, related_name='assigned_tracking_records')
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE, related_name='received_tracking_records')
    assign_date = models.DateField(default=now)
    return_date = models.DateField(null=True,blank=True)
    condition_checkout = models.TextField()

    def __str__(self):
        return f"{self.employee.e_name}-{self.device.type}-{self.assign_date}"
