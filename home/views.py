from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples = [
        {'name': 'Abhijeet Gupta', 'age': 26},
        {'name': 'Rohan Sharma', 'age': 23},
        {'name': 'vicky Kaushal', 'age': 28},
        {'name': 'Deepanshu Agrawal', 'age': 20},
        {'name': 'Sandip Chauhan', 'age': 17}
    ]

    vegetable = ['Pumpkin','Tomato','Potatoe']

    return render(request, "home/index.html", context={'page':'Django 2024 Tutorial', 'peoples': peoples,'vegetable': vegetable})

def contact(request):
    context={'page':'Contact'}
    return render(request, "home/contact.html", context )

def about(request):
    context={'page':'About'}
    return render(request, "home/about.html", context)

