from django.urls import path
from binathi import views

urlpatterns=[
   path('',views.home,name='home'),
   path('demo/',views.chk),
   path('hm/',views.homepage),
   path('lg/',views.lgn),
   path('rg/',views.reg,name='register'),
   path('ht/',views.bthm),
   path('ab/',views.about,name='about'),
   path('co/',views.contact,name='contact'),
]