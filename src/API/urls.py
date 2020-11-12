from django.urls import path


from .views import PollListView, PollDetailView, AnswerCreateView, AnswerListView


urlpatterns = [
    path('poll', PollListView.as_view()),
    path('poll/<int:poll_id>', PollDetailView.as_view()),
    path('poll/answer', AnswerCreateView.as_view()),
    path('answer/<int:user_id>', AnswerListView.as_view()),
]
