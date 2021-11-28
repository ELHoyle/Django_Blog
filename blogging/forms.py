from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from blogging.models import Post, Category


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]
        help_texts = {
            "title": _("Max length = 128 characters"),
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ("name",)
        labels = {
            "name": _("Category"),
        }
