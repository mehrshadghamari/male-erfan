from math import trunc
from turtle import update
from venv import create
from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=25)
    content=models.TextField()
    create_time=models.DateTimeField(auto_now=True)
    update_time=models.DateTimeField(auto_now_add=True)
