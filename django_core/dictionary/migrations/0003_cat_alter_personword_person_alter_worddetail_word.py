# Generated by Django 4.1.1 on 2022-09-15 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0002_personword_word_wordstat_worddetail_personword_word'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('color', models.CharField(max_length=16)),
                ('birth_year', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='personword',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='dictionary.person'),
        ),
        migrations.AlterField(
            model_name='worddetail',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words_detail', to='dictionary.personword'),
        ),
    ]