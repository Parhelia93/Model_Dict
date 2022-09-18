from rest_framework import serializers
from .models import Cat, Owner, Achievement, AchievementCat, Person, PersonWordList, Word, WordStat, WordDetail


class OwnerSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'cats') 


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = ('id', 'name') 


class CatSerializer(serializers.ModelSerializer):
    #owner = serializers.StringRelatedField(read_only=True)
    #read_only=True,
    achievements = AchievementSerializer(many=True)

    class Meta:
        model = Cat
        fields = ('name', 'color', 'birth_year', 'owner', 'achievements')

    def create(self, validated_data):
        # Уберем список достижений из словаря validated_data и сохраним его
        print(validated_data)
        achievements = validated_data.pop('achievements')

        # Создадим нового котика пока без достижений, данных нам достаточно
        cat = Cat.objects.create(**validated_data)

        # Для каждого достижения из списка достижений
        for achievement in achievements:
            # Создадим новую запись или получим существующий экземпляр из БД
            current_achievement, status = Achievement.objects.get_or_create(
                **achievement)
            # Поместим ссылку на каждое достижение во вспомогательную таблицу
            # Не забыв указать к какому котику оно относится
            AchievementCat.objects.create(
                achievement=current_achievement, cat=cat)
        return cat


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('user', 'telegram_id') 

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('word',) 

class WordStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordStat
        fields = ('true_answer', 'false_answer') 

class WordDetailSerializer(serializers.ModelSerializer):
    word_stat = WordStatSerializer()
    class Meta:
        model = WordDetail
        fields = ('translate', 'example', 'date_add', 'word_stat')


class PersonWordListSerializer(serializers.ModelSerializer):
    word = WordSerializer(many=True, read_only=True)
    person = PersonSerializer(read_only=True)
    words_detail = WordDetailSerializer(many=True, read_only=True)
    class Meta:
        model = PersonWordList
        fields = ('person', 'word', 'date_add', 'slug', 'words_detail')

class UpdatePersonWordSerializer(serializers.ModelSerializer):
    word = WordSerializer()
    person = PersonSerializer()
    words_detail = WordDetailSerializer()
    class Meta:
        model = PersonWordList
        fields = ('person', 'word', 'words_detail')