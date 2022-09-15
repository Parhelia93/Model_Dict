from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.user.username


class Word(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.word


class PersonWord(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)    #on_delete ???
    person = models.ForeignKey(Person,  related_name='words', on_delete=models.CASCADE)    #on_delete ???
    date_add = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50)

    def __str__(self) -> str:
        return self.word


class WordStat(models.Model):
    true_answer = models.IntegerField()
    false_answer = models.IntegerField()


class WordDetail(models.Model):
    translate = models.CharField(max_length=50)
    example = models.TextField(max_length=150)
    word = models.ForeignKey(PersonWord, related_name='words_detail', on_delete=models.CASCADE)  #on_delete ???
    date_add = models.DateTimeField(auto_now_add=True)
    word_stat = models.OneToOneField(WordStat, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.translate


"""For test API"""
class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    birth_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
