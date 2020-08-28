from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import  query_Serializer
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

def message_list(request):

    if request.method == 'POST':
        print(request.body)
        #var=json.loads(request.body)
        input_question=request.POST.get("messages")
        nlp_output = nlp_out.respond(input_question)
        final_out = response_generation(nlp_output, input_question)
        print(final_out)
        query_serializer=query_Serializer(final_out)
        question=None
        try:
            question=Query.objects.get(question=input_question)

        except Query.DoesNotExist:
            pass

        if question :
            #return Response({"message" : question.response} , status=200)
            return Response(query_serializer.data , status=200)

        else :
            return Response({"message" : "Your question is not there"} , status=200)


        body = {"message":"The question you asked is {} ".format(input_question)}
        return Response(body, status=200)
