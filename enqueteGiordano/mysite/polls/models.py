"""Vai passar as informações do site para o banco de dados"""
import datetime

from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= datetime.timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # Lá na tabela question, toda pergunta vai ter uma tabela, um id. o ForeignKey() vai se balizar ali.
    # Caso eu apague uma pergunta o on_delete vai apagar todas as alternativas
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
