from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from brain import scrape
import json
import re
from .models import fur
from .serializers import furSerializer
from rest_framework import viewsets, filters, generics
from django.views.decorators.csrf import csrf_exempt

class furViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = fur.objects.all()
    serializer_class = furSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['imdbID']

def index(request):
    return render(request, 'indexSingle.html')

@csrf_exempt
def return_data(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        imdbID = data['ID']
        print("pacman")
    
    quotes = []
    
    dblength = fur.objects.count()
    
    flag = 0

    for i in range(1, dblength+1):
               
        try:
            instance = fur.objects.get(id=i)
        except fur.DoesNotExist:
            i = i + 1

        if imdbID == instance.imdbID:
            new_instance = fur.objects.get(id=i)
            flag = 1
            return JsonResponse({'quotes': json.loads(new_instance.quotes)})

    if flag == 0:

        try:
            quotes = scrape.scrape_quotes(imdbID)
        except:
            return JsonResponse({'quotes': []})

        jquotes = json.dumps(quotes)
        new_instance = fur(imdbID=imdbID, quotes=jquotes)
        new_instance.save()
        return JsonResponse({'quotes': quotes})