# Generated by Django 4.1.1 on 2022-09-18 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0005_achievement_achievementcat_cat_achievements'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonWordList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='dictionary.person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonWordListWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.personwordlist')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.word')),
            ],
        ),
        migrations.AddField(
            model_name='personwordlist',
            name='word',
            field=models.ManyToManyField(through='dictionary.PersonWordListWord', to='dictionary.word'),
        ),
        migrations.AlterField(
            model_name='worddetail',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words_detail', to='dictionary.personwordlist'),
        ),
        migrations.DeleteModel(
            name='PersonWord',
        ),
    ]
