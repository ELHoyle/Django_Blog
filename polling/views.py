from django.contrib.auth import login
from django.shortcuts import render
from django.http import Http404
from polling.models import Poll
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
