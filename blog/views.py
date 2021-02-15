from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import EditForm, PostForm
from .models import Category, Post


class HomeView(generic.ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


def category_list_view(request):
    category_list_menu = Category.objects.all()
    return render(request, 'category_list.html', {'category_list_menu': category_list_menu})


def category_view(request, category):
    category_posts = Post.objects.filter(category=category.replace('-', ' '))
    return render(request, 'categories.html', {'category': category.title().replace('-', ' '),
                                               'category_posts': category_posts})


class ArticleDetailView(generic.DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['category_menu'] = category_menu
        return context


class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCategoryView(generic.CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
