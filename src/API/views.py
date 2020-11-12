from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone


from .models import Poll
from .serializers import PollListSerializer, PollDetailSerializer, AnswerCreateSerializer, AnswerListSerializer


class PollListView(generics.ListAPIView):
    queryset = Poll.objects.filter(end_date__gte=timezone.now())
    serializer_class = PollListSerializer


class PollDetailView(APIView):

    def get(self, request, poll_id):
        try:
            poll = Poll.objects.get(id=poll_id)
        except Poll.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PollDetailSerializer(poll)
        return Response(serializer.data)


class AnswerCreateView(APIView):

    def post(self, request):
        serializer = AnswerCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        print(serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class AnswerListView(APIView):

    def get(self, request, user_id):
        try:
            polls = Poll.objects.filter(questions__answer__user=user_id)
        except Poll.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AnswerListSerializer(polls, many=True)
        return Response(serializer.data)
