from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import  query_Serializer
from rest_framework.decorators import api_view
from .nlp_module import nlp_module
from .response_generator import response_generation, sample
import json

from .models import Note, Query, Unanswered_Query

nlp_out = nlp_module()


@api_view(['POST'])
@csrf_exempt

def message_list(request):

    if request.method == 'POST':
        print(request.body)
        input_question=request.POST.get("messages")
        nlp_output = nlp_out.respond(input_question)

        final_out = response_generation(nlp_output, input_question)

        if final_out == sample :
            return Response({"message": final_out}, status=404)

        query_serializer=query_Serializer(final_out)

        #if query_serializer.is_valid():
        #    return Response(query_serializer.data, status=200)

        #return Response({"message": final_out}, status=404)

        return Response(query_serializer.data, status=200)
