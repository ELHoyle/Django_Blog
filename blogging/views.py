from django.db.models.query import QuerySet
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from blogging.models import Post
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    post = queryset
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    published = queryset
    template_name = "blogging/detail.html"


def about_view(request):
    description = """This blog was created using the Django web framework by Eric Hoyle as 
    the culmination of a year long study of python programming through the UW 
    Professional and Continuing Education Programming in Python certificate
    course.
    """
    context = {"description": description}
    return render(request, "blogging/about.html", context)
