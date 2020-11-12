from django.db import models
from django.utils import timezone


class Poll(models.Model):
    name = models.CharField('Название опроса', max_length=200, blank=False)
    description = models.TextField('Описание опроса')
    begin_date = models.DateTimeField('Начало опроса', default=timezone.now)
    end_date = models.DateTimeField('Конец опроса', default=timezone.now() + timezone.timedelta(hours=4))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    TYPE_QUESTION = (
        ('TXT', 'Текстовый'),
        ('ONE', 'Один вариант'),
        ('MUL', 'Несколько вариантов')
    )
    description = models.CharField('Описание вопроса', max_length=500, blank=False)
    type = models.CharField('Тип вопроса', max_length=3, choices=TYPE_QUESTION, blank=False)
    poll = models.ForeignKey('Poll', blank=False, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    text = models.TextField('Описание выбора', blank=False)
    right = models.BooleanField('Правильность ответа', default=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Выбор'
        verbose_name_plural = 'Выборы'


class Answer(models.Model):
    user = models.IntegerField('ID пользователя', blank=False)
    text = models.TextField('Текстовый ответ', blank=True)
    choice = models.ManyToManyField('Choice', blank=True)
    question = models.ForeignKey('Question', blank=False, on_delete=models.CASCADE, related_name='answer')

    def __str__(self):
        return self.user
