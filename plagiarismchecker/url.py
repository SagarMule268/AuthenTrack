from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='plagiarism-check-mainpage'),
    path('compare/', views.fileCompare,name='compare'), 
    path('test/', views.test,name='Test'),
    path('filetest/', views.filetest,name='filetest'),
    path('twofiletest1/', views.twofiletest1,name='twofiletest1'),
    path('twofilecompare1/', views.twofilecompare1,name='twofilecompare1'),
    path('documentUpload/', views.documentUpload,name='documentUpload'),
    path('textUpload/', views.textUpload,name='textUpload'),
    path('comparetextCheck/', views.comparetextCheck,name='comparetextCheck'),
    path('comparefilecheck/', views.comparefilecheck,name='comparefilecheck'),
    path('help/', views.helpus, name='helpus'),
    path('contactus/', views.contactus, name='contactus'),
    





]
