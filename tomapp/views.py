from django.shortcuts import render

# Create your views here.

#-*- coding: utf-8 -*-

from django.http import HttpResponse, Http404

def home(request):
    text = "<h1>Bienvenue sur mon blog</h1>"
    return HttpResponse(text)

def view_article(request, id_article):
    if int(id_article) > 100:
        raise Http404
    return HttpResponse('<h1>Mon article ici</h1>')
##    text = "Vous avez demande larticle n{0} !".format(id_article)
##    return HttpResponse(text)

def list_articles(request, month, year):
    text = "Vous avez demande les articles de {0} {1}.".format(month, year)
    return HttpResponse(text)
