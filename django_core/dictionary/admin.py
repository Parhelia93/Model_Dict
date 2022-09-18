from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Person)
admin.site.register(Word)
admin.site.register(PersonWordList)
admin.site.register(PersonWordListWord)
admin.site.register(WordStat)
admin.site.register(WordDetail)
admin.site.register(Cat)