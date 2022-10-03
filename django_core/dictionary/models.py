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


class PersonWordList(models.Model):
    # word = models.ManyToManyField(Word, through='PersonWordListRelation') 
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    person = models.ForeignKey(Person,  related_name='words', on_delete=models.CASCADE)    
    date_add = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50)

    def __str__(self) -> str:
        return str(self.word)


# class PersonWordListRelation(models.Model):
#     word = models.ForeignKey(Word, on_delete=models.CASCADE)
#     person_list = models.ForeignKey(PersonWordList, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.word} {self.person_list}'


class WordStat(models.Model):
    true_answer = models.IntegerField()
    false_answer = models.IntegerField()

    


class WordDetail(models.Model):
    translate = models.CharField(max_length=50)
    example = models.TextField(max_length=150)
    word = models.ForeignKey(PersonWordList, related_name='words_detail', on_delete=models.CASCADE)  
    date_add = models.DateTimeField(auto_now_add=True)
    word_stat = models.OneToOneField(WordStat, related_name='word_stat', on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.translate


"""For test API"""
class Achievement(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name



class Owner(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    birth_year = models.IntegerField(blank=True, null=True)
    owner = models.ForeignKey(
        Owner, related_name='cats', on_delete=models.CASCADE)
    achievements = models.ManyToManyField(Achievement, through='AchievementCat')

    def __str__(self):
        return self.name



class AchievementCat(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.achievement} {self.cat}'
