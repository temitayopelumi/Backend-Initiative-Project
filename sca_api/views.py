# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

def Users(request):
    responseData = {
        'id': 1,
        'name': 'Adaobi olalekan',
    }

    return JsonResponse(responseData)

def Movies(request):
    responseData = {
        'id': 1,
        'name': 'Got',
        'details' : 'Game of Thrones'
    }

    return JsonResponse(responseData)

def Rentals(request):
    responseData = {
        'id': 4,
        'name': 'Test Response',
        'roles' : ['Admin','User']
    }

    return JsonResponse(responseData)

