from django.comf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
]
