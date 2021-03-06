from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from blogging.models import Post
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogging.forms import PostForm, CategoryForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required
def add_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        category_form = CategoryForm(request.POST)
        if post_form.is_valid() and category_form.is_valid():
            category = category_form.save()
            post = post_form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.published_date = timezone.now()
            post.save()
            category.posts.add(post)

            return redirect("/")
    else:
        post = PostForm()
        category = CategoryForm()
        return render(request, "blogging/add_post.html", {"forms": [post, category]})


@method_decorator(login_required, name="dispatch")
class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    post = queryset
    template_name = "blogging/list.html"


@method_decorator(login_required, name="dispatch")
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
