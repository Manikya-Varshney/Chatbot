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


@api_view(['POST'])
@csrf_exempt

#def index(request, question):
#    answer = Query.objects.get(question=question).response
#    return HttpResponse(answer)

def message_list(request, sender=None, receiver=None):

    if request.method == 'POST':
        print(request.body)
        var=json.loads(request.body)
        input_question=var["messages"]
        nlp_output = nlp_out.respond(input_question)
        final_out = response_generation(nlp_output, input_question)
        body = {"message": final_out}
        return JsonResponse(body, status=200)
