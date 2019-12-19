
# from django.conf.urls import url
from django.urls import path
from LFourApp import views


# TEMPLATE TAGGING
app_name = 'LFourApp'   # important to have for relative urls

urlpatterns = [
    # url(r'^relative/', views.relative, name='relative'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
