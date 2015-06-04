from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.shortcuts import render_to_response
import json
import os
import datetime

json_data = open('starter/data/movies.json')
data = json.load(json_data)

def landing_page(request):
    return render(request, "starter/landing_page.html")

def movielist(request):
    return render_to_response('baselist.html', {'movies':data[0]['movies']})
def getmovie(request, movie_id=0):
    return render_to_response('basedetail.html', {'ti': movie_id, 'movies':data[0]['movies']})
    
                     
