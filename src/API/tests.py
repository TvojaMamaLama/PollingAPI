import json
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse
from rest_framework import status


from .models import Poll, Question, Choice, Answer


client = Client()


class ApiTest(TestCase):

    def setUp(self):
        poll = Poll.objects.create(
            name='Первый настоящий опрос',
            description='Проверяем возможности апи',
            begin_date=timezone.now,
            end_date=timezone.now() + timezone.timedelta(hours=4),
        )
        question = Question.objects.create(
            description='Кто ел устрицы?',
            type='ONE',
            poll=poll
        )
        choice = Choice.objects.create(text='Я', right=True, question=question)
        Answer.objects.create(user=123, choice=choice, question=question)

    def okStatusGetPollListTest(self):
        response = client.get(reverse('get_poll_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def okStatusPollDetailTest(self):
        response = client.get('api/v1/poll/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def createStatusCreateAnswerTest(self):
        data = {
            'user': 1234567,
            'choice': 1,
            'question': 1,
        }
        response = client.post(
            reverse('create_answer'),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def badStatusCreateAnswerTest(self):
        data = {
            'choice': 1,
            'question': 1,
        }
        response = client.post(
            reverse('create_answer'),
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def okStatusAnswersTest(self):
        response = client.get('api/v1/poll/answer/123')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
