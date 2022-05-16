from multiprocessing import context
from pdb import post_mortem
from turtle import title
from django.shortcuts import render
from app1.models import Post
from django.http import HttpResponse
# Create your views here.

def home(request):
   obj_list= Post.objects.all()


   context={'obj_list':obj_list}
   
   return render(request, 'app1/list.html',context )


def detail(request,id):
   obj=Post.objects.get(pk=id)
   context={'obj':obj}
   return render (request,'app1/detail.html',context)
