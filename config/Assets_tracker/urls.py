from django.urls import path
from . views import company_view,employee_view,device_view,tracking_view,homeview
urlpatterns = [
    path('',homeview,name='homeview'),
    path('c_view/',company_view,name='company_view'),
    path('e_view/',employee_view,name='employee_view'),
    path('d_view/',device_view,name='device_view'),
    path('t_view/',tracking_view,name='tracking_view'),
    # path('view/',list_view,name='list_view'),
]