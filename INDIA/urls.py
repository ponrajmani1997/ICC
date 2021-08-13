from django.urls import path
from django.urls.resolvers import URLPattern
from INDIA.views import *

app_name='INDIA'

urlpatterns=[
    path('IND/',IND,name='IND'),
    path('TEAMINDIA/',TEAMINDIA,name='TEAMINDIA'),
]