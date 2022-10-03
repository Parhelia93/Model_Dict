from .models import WordDetail, PersonWordList, WordDetail
from django.db.models.query import QuerySet
from .chat_settings import PRIORITY_DIFFERENCE_STAT_CNT
import random

def get_random_word(person_list: QuerySet[PersonWordList]) -> WordDetail: 
    high_priority_words = []
    low_priority_words = []
    for person_word in person_list:
        person_word_details = WordDetail.objects.filter(word=person_word)
        for person_word_detail in person_word_details:
                if person_word_detail.word_stat.false_answer - person_word_detail.word_stat.true_answer >= PRIORITY_DIFFERENCE_STAT_CNT:
                    high_priority_words.append(person_word_detail)
                else:
                    low_priority_words.append(person_word_detail)
    if len(high_priority_words):
        return random.choice(high_priority_words)
    elif len(low_priority_words):
        return random.choice(low_priority_words)
    return None