from django.urls import path
from . views import company_view,employee_view,device_view,tracking_view,homeview,update_view,CompanyList, CompanyDetail, EmployeeList, EmployeeDetail, DeviceList, DeviceDetail, TrackingList, TrackingDetail



urlpatterns = [
    path('',homeview,name='homeview'),
    path('c_view/',company_view,name='company_view'),
    path('e_view/',employee_view,name='employee_view'),
    path('d_view/',device_view,name='device_view'),
    path('t_view/',tracking_view,name='tracking_view'),
  
    path('update/<int:id>/',update_view,name='update_view'),

    path('companies/', CompanyList.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetail.as_view(), name='company-detail'),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),
    path('devices/', DeviceList.as_view(), name='device-list'),
    path('devices/<int:pk>/', DeviceDetail.as_view(), name='device-detail'),
    path('tracking/', TrackingList.as_view(), name='tracking-list'),
    path('tracking/<int:pk>/', TrackingDetail.as_view(), name='tracking-detail'),
]
