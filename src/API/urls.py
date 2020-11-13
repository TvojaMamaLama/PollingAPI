from django.urls import path


from .views import PollListView, PollDetailView, AnswerCreateView, AnswerListView


urlpatterns = [
    path('poll', PollListView.as_view(), name='get_poll_list'),
    path('poll/<int:poll_id>', PollDetailView.as_view(), name='poll_detail'),
    path('poll/answer', AnswerCreateView.as_view(), name='create_answer'),
    path('answer/<int:user_id>', AnswerListView.as_view(), name='get_answers'),
]
