from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('SyncHeart', views.heartback, name='heartback'),
    path('DownParam', views.sysetup, name='sysetup'),
    path('SyncCustomer', views.synperson, name='synperson'),
    path('SyncInOutRecord', views.synrecord, name='synrecord'),
    path('UploadErr', views.errback, name='errback'),
]