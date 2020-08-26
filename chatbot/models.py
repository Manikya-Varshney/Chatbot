from django.db import models


class Note(models.Model):
    text = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Query(models.Model):
    question = models.CharField(max_length=2000)
    response = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return 'Question: {question}, Answer: {answer}'.format(question=self.question, answer=self.response)

    class Meta:
        verbose_name_plural = 'Queries'


class Unanswered_Query(models.Model):

    unanswered_query = models.CharField(max_length=2000)

    def __str__(self):
        return 'Query: {unanswered_query}'.format(unanswered_query=self.unanswered_query)
