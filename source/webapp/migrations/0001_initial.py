# Generated by Django 2.2 on 2019-09-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('text', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Описание')),
                ('status', models.CharField(choices=[('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')], default='new', max_length=20, verbose_name='Статус')),
                ('deadline', models.DateField(blank=True, max_length=20, null=True, verbose_name='Срок сдачи')),
            ],
        ),
    ]