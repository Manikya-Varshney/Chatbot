sample = "Sorry, cannot understand the question from provided information. Please try again or Do you want to connect to our assistant?"

def response_generation(s,input_question):
    """ Function to generate appropriate response to the user input.

    The response generator module is responsible for retrieving response from the database based upon the input question.
    question is one of the questions that are pre-defined in the database and there is a corresponding response to each of the questions in the database.
    The response generator is basically a function that takes two inputs, "input_question" which is the exact query the user asked and a string "s" whose
    value is the question that nlp engine found out or -1 if it is not in the database.
    Since we are using DJango framework, database is already connected to the framework. So we just need to import that “connection”.
    If the value of s is -1 then we store the asked query in a table and return the response "Sorry, cannot understand the question from provided information.".
    If s is not equal to -1, we match the question with all the pre-defined questions in the database and the corresponding answer is stored in the cursor
    We convert this list to string and return the response.

    Args:
        s: The question found by the nlp engine or -1 if it is not in the database.
        input_question: The exact query that the user asked.

    """

    from django.db import connection
    from .models import Query, Unanswered_Query
    with connection.cursor() as cursor1:

        if s==-1:

            try:
                cursor= Unanswered_Query.objects.get(unanswered_query=input_question)
                return sample
            except:
                cursor= Unanswered_Query.objects.create(unanswered_query=input_question)
                return sample

            return sample

        cursor=Query.objects.get(question=s)
        return cursor
