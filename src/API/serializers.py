from rest_framework import serializers


from .models import Poll, Question, Choice, Answer


class PollListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class PollDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Poll
        fields = '__all__'


class AnswerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class QuestionAnswerSerializer(serializers.ModelSerializer):
    answer = AnswerCreateSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class AnswerListSerializer(serializers.ModelSerializer):
    questions = QuestionAnswerSerializer(many=True)

    class Meta:
        model = Poll
        exclude = ('begin_date', 'end_date')
