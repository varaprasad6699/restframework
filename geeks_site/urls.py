"""geeks_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    path("",home), 
    path('post/',postdata),
    path('getone/<int:pk>',getdataofparticular),
    path('updateone/<int:pk>',updatedataofparticular),
    path('deleteone/<int:pk>',deletedataofparticular)
"""
from django.contrib import admin
from django.urls import path,include
from geeks_app.views import EmployeeAll
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('api',EmployeeAll,basename="employee")
""" from geeks_app.views import home,postdata,getdataofparticular,updatedataofparticular,deletedataofparticular """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]

 