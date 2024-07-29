"""
URL configuration for pr14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path
from app14.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("n",cv2.as_view(),name="cv2"),
    path("",employeecreate.as_view(),name="employeecreate"),
    path('retrieve/',employeeretrieve.as_view(),name="employeeretrieve"),
    path('retrieve/<int:pk>',employeedetail.as_view(),name='employeedetail'),
    path('<int:pk>/update/',employeeupdate.as_view(),name='employeeupdate'),
    path('<int:pk>/delete/',employeedelete.as_view(),name='employeedelete')
]
