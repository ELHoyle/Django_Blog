from io import DEFAULT_BUFFER_SIZE
from django.urls import path
from polling.views import PollListView, PollDetailView, create_poll

urlpatterns = [
    path("", PollListView.as_view(), name="poll_index"),
    path("polls/<int:pk>/", PollDetailView.as_view(), name="poll_detail"),
    path("post/", create_poll, name="create_poll"),
]
