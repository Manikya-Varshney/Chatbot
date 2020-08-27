def response_generation(s,input_question):
    """ Function to generate appropriate response to the user input.

    The response generator module is responsible for retrieving response from the database based upon the question that the back-end provides.
    question is one of the questions that are pre-defined in the database and there is a corresponding response to each of the questions in the database.
    The response generator is basically a function that takes two inputs, "input_question" which is the exact query the user asked and a string "s" whose
    value is the question that nlp engine found out or -1 if it is not in the database.
    Since we are using DJango framework, database is already connected to the framework. So we just need to import that “connection”.
    Once we import connection from django.db, we can search anything in the database by the help of “cursor” object.To execute the queries on the database we need a cursor object.
    It is plays a similar role to that of a file handle for files.
    If the value of s is -1 then we store the asked query in a table and return the response "Sorry, cannot understand the question from provided information.".
    If s is not equal to -1, we match the question with all the pre-defined questions in the database by executing an sql query and the corresponding answer is stored in the cursor
    in the form of list of tuples. In this case the list will only have a single tuple.
    We convert this list to string and return the response to backend.


    Args:
        s: The question found by the nlp engine or -1 if it is not in the database.
        input_question: The exact query that the user asked.

    Returns:
        string: s2- A string type variable that contains the appropriate response to the user query
    """
    from django.db import connection
    with connection.cursor() as cursor:   # creates a database cursor object called "cursor" which enables us to run sql queries on the database
        if s==-1:
            cursor.execute("SELECT * FROM Unanswered_query") # extracts all the data from the table.
            for x in cursor:      # for loop is used to check if the input_question is already present in the table or not. If it is present then no need to add it again.
                if x[0]==input_question:
                    s2="Sorry, cannot understand the question from provided information."
                    return s2
            try:
                cursor.execute("INSERT INTO Unanswered_query(unanswered_query) VALUES(%s)",[input_question]) # adds input_question to the table. Try block is there just to avoid any unforeseen errors.
            except:
                pass
            s2="Sorry, cannot understand the question from provided information."
            return s2
        sql_query=("SELECT response from Query WHERE question=%s") # creation of sql query to search the database
        cursor.execute(sql_query,[s])  # executes the query and returns a list of tuples to cursor
        # cursor contains the "response".
        # We need to traverse the cursor to get the "response" in string form.
        for x in cursor:
            s1=x
        s2=''.join(s1) # creates the response string
    return s2 # returns the string
