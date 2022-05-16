from django.urls import path
from . import views

urlpatterns =[
    path('home/',views.home),
    path('detail/<int:id>',views.detail),
]