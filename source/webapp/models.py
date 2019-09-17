from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Tracker(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Название')
    text = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    status = models.CharField(max_length=20, verbose_name='Статус', default=STATUS_CHOICES[0][0],
                                choices=STATUS_CHOICES)
    deadline = models.DateField(max_length=20, verbose_name='Срок сдачи', null=True, blank=True)

    def __str__(self):
        return self.title

