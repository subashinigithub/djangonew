from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class cv2(View):
    def get(self,r):
        return HttpResponse('response')
from .models import employee
from .forms import employeeform
from django.views.generic.edit import CreateView

class employeecreate(CreateView):
    model=employee
    fields='__all__'
    success_url='/n'

from django.views.generic.list import ListView
class employeeretrieve(ListView):
    model=employee

from django.views.generic.detail import DetailView
class employeedetail(DetailView):
    model=employee

from django.views.generic.edit import UpdateView
class employeeupdate(UpdateView):
    model=employee
    fields='__all__'
    success_url='/n'

from django.views.generic.edit import DeleteView
class employeedelete(DeleteView):
    model=employee
    success_url='/n'




