from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .service import words_repeated, validate_url

# Create your views here.

def home(request):
    return render(request, 'word/index.html')

class WordsRepeated(APIView):
    def post(self, request):
        try:
            url = request.data['url']            
            if validate_url(url):
                return Response(words_repeated(url))
            else:
                return HttpResponse('invalid url')
        except AssertionError:
            return HttpResponse("a error has ocurred")
        except KeyError:
            return HttpResponse("a error has ocurred")
        