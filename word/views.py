from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response

from rest_framework.views import APIView

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the API!")

class WordsRepetead(APIView):
    def post(self, request):
        print(request.data['url'])
        
        data={
            'url': request.data['url']
            }
        return Response(data)