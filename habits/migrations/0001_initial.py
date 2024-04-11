# Generated by Django 5.0.3 on 2024-04-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='Место выполнения')),
                ('time', models.TimeField(verbose_name='Время начала выполнения')),
                ('action', models.CharField(max_length=100, verbose_name='Действие')),
                ('sign_nice_habit', models.BooleanField(default=False, verbose_name='Признак приятной привычки')),
                ('interval', models.CharField(choices=[('once_a_day', 'Один раз в день'), ('once_a_two_day', 'Один раз в два дня'), ('once_a_three_day', 'Один раз в три дня'), ('once_a_four_day', 'Один раз в четыре дня'), ('once_a_five_day', 'Один раз в пять дней'), ('once_a_six_day', 'Один раз в шесть дней'), ('once_a_week', 'Один раз в неделю')], default='once_a_day', max_length=100, verbose_name='Периодичность')),
                ('reward', models.CharField(blank=True, max_length=200, null=True, verbose_name='Награда')),
                ('duration_time', models.TimeField(verbose_name='Время выполнения')),
                ('is_public', models.BooleanField(default=False, verbose_name='Публичная привычка')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
        migrations.CreateModel(
            name='NiceHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_nice_habit', models.BooleanField(default=False, verbose_name='Признак приятной привычки')),
                ('action', models.CharField(max_length=100, verbose_name='Действие')),
            ],
            options={
                'verbose_name': 'Приятная привычка',
                'verbose_name_plural': 'Приятные привычки',
            },
        ),
    ]
