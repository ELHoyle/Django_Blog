from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import Http404
from polling.models import Poll
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from polling.forms import PollForm


@login_required
def create_poll(request):
    if request.method == "POST":
        poll_form = PollForm(request.POST)
        if poll_form.is_valid():
            poll_form.save()
            return redirect("/polling/")
    else:
        poll_form = PollForm()
        return render(request, "polling/create_poll.html", {"form": poll_form})


@method_decorator(login_required, name="dispatch")
class PollListView(ListView):
    model = Poll
    template_name = "polling/list.html"


@method_decorator(login_required, name="dispatch")
class PollDetailView(DetailView):
    model = Poll
    template_name = "polling/detail.html"

    def post(self, request, *args, **kwargs):
        poll = self.get_object()

        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

        context = {
            "poll": poll,
            "title": poll.title,
        }
        return render(request, "polling/detail.html", context)


# Create your views here.
