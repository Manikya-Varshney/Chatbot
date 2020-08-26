from django.shortcuts import render
from django.http import HttpResponse

from . import nlp_module
from .models import Note, Query

def index(request, question):
    answer = Query.objects.get(question=question).response
    return HttpResponse(answer)
