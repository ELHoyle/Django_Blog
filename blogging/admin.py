from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from blogging.models import Post, Category

# admin.site.register(Post)
# admin.site.register(Category)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ["name", "description"]


class CategoryInline(admin.StackedInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ("text", "title", "author", "published_date")
    exclude = ("categories",)
    inlines = [
        CategoryInline,
    ]
