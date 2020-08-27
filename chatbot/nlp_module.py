from sentence_transformers import SentenceTransformer
import scipy.spatial
import string
from .models import Query

class nlp_module:
    """
    nlp_module class for handling NLP tasks.

    It takes in questions and computes feature vector representation of the questions.
    Then whenever user text is passed, the best matching questions from above are returned.

    1. remove_punct_dict (dict) : Constains puncuations to be removed from any input text
    2. embedder(SentenceTransformer) : Pretrained BERT Model to convert input text to feature vectors
    3. questions(list) : Contains the list of questions obtained from the database
    4. corpus(list) : Contains the list of questions in lower case, without punctuations
    5. corpus_embeddings(list(numpy.ndarray)) : list of feature vectors of questions
    """

    def __init__(self):
        """
        Constructor for nlp_module class.
        """

        self.remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
        self.embedder = SentenceTransformer('bert-base-nli-mean-tokens')
        '''
        This method 'self.embedder' will download a bert-base-nli-mean-tokens model for embeddings and vectorisation.
        If you find a 'FileNotFoundError' than
        delete everything placed in the torch cached folder:
        for example in your case 'C:/Users/a324448/.cache/torch/sentence_transformers'.
        If nothing works than download the 'bert-base-nli-mean-tokens' model from
        https://public.ukp.informatik.tu-darmstadt.de/reimers/sentence-transformers/v0.2/
        '''
        self.questions = self.getData()
        self.corpus = self.questions.lower().translate(self.remove_punct_dict).splitlines()
        self.questions=self.questions.splitlines()
        self.corpus_embeddings = self.embedder.encode(self.corpus)

    def getData(self):
        """
        `getData` function obtains the list of questions from the database.
        The questions are returned as a single string where the individual questions are separated
        by a `\n` character.

        Returns:
            data : single string containing all the questions
        """

        data = ""
        queries_all = Query.objects.all()
        for q in queries_all:
            data += "\n" + q.question
        data = data[1:]
        return data

    def respond(self, query):
        """
        `respond` function takes the user query, computes its feature vector and
        compares with the feature vectors of predefined questions.

        Args:
            query(string) : The user query

        Returns:
            question(string) : The question that best matches with the user query
        """
        query.lower().translate(self.remove_punct_dict)
        query_embedding=self.embedder.encode([query])[0]
        distances = scipy.spatial.distance.cdist([query_embedding], self.corpus_embeddings, "cosine")[0]
        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])

        max_score=1-results[0][1]
        if max_score>0.75:
            return self.questions[results[0][0]]
        else:
            return -1
