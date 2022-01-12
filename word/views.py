from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .service import words_repeat

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the API!")

class WordsRepetead(APIView):
    def post(self, request):
        try:
            url = request.data['url']        
            return Response(words_repeat(url))
        except AssertionError:
            return HttpResponse("a error has ocurred")
        except KeyError:
            return HttpResponse("a error has ocurred")
        