from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from queries.serializers import  query_Serializer
from rest_framework.decorators import api_view
from .nlp_module import nlp_module
from .response_generator import response_generation
import json

from .models import Note, Query, Unanswered_Query

nlp_out = nlp_module()

def index(request, question):
    answer = Query.objects.get(question=question).response
    return HttpResponse(answer)
