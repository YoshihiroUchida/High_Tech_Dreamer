from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject

def index(request):
 subjects = Subject.objects.all()
 context = { 'subjects_list': subjects,}
 print(context)
 return render(request, 'index.html', context)
