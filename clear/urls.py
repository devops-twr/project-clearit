from django.urls import path
from . import views

#Create your urls here.
urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('course/',views.course,name='course'),
    # path('index-02/', views.index_02, name='index-02'),
    path('careers/',views.careers,name='careers'),
    path('aws/', views.aws, name='aws'),
    path('python/', views.python, name='python'),
    path('java/', views.java, name='java'),
    path('datascience/', views.datascience, name='datascience'),
   path('callbackForm/', views.callbackForm, name='callbackForm'),
    path('advanceexcel/', views.advanceexcel, name='advanceexcel'),
]