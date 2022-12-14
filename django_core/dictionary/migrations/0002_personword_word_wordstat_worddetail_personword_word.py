# Generated by Django 4.1.1 on 2022-09-13 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.person')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WordStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('true_answer', models.IntegerField()),
                ('false_answer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WordDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translate', models.CharField(max_length=50)),
                ('example', models.TextField(max_length=150)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.personword')),
                ('word_stat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dictionary.wordstat')),
            ],
        ),
        migrations.AddField(
            model_name='personword',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.word'),
        ),
    ]
