from django.shortcuts import render
from django.views import generic
from .models import Post, Category, Tag

# Create your views here.
class PostList(generic.ListView):
    model = Post
    ordering = '-created_at'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tag_list'] = Tag.objects.all()
        return context

class PostDetail(generic.DetailView):
    model = Post




