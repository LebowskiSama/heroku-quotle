from django.shortcuts import render, HttpResponseRedirect
from brain import scrape
import json
import re
from monkey.models import fur

def index(request):
    return render(request, 'index.html')

def return_data(request):

    search_term = request.POST['search']

    quotes = []
    
    try:
        mname, imdbID =  scrape.parse_titles(search_term)
    except KeyError:
        return render(request, 'notfound.html')
        return HttpResponseRedirect('')

    dblength = fur.objects.count()
    
    flag = 0

    for i in range(1, dblength+1):
        
        try:
            instance = fur.objects.get(id=i)
        except fur.DoesNotExist:
            i = i + 1

        if mname == instance.title:
            new_instance = fur.objects.get(id=i)
            jsondec = json.decoder.JSONDecoder()
            quotes = jsondec.decode(new_instance.quotes)
            flag = 1
            break

    if flag == 0:
        try:
            quotes = scrape.scrape_quotes(imdbID)
        except IndexError:
            return render(request, 'noquotes.html')
            return HttpResponseRedirect('')

        jquotes = json.dumps(quotes)
        new_instance = fur(title=mname, quotes=jquotes)
        new_instance.save()

    context = {}
    context['mname'] = mname
    context['quotes'] = quotes

    return render(request, 'quotes.html', context)
    return HttpResponseRedirect('')