from django.urls import reverse_lazy
from django.views import generic

from .forms import EditForm, PostForm
from .models import Post


# def home(request):
#     return render(request, 'home.html', {})


class HomeView(generic.ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class ArticleDetailView(generic.DetailView):
    model = Post
    template_name = 'article_detail.html'


class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'


class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
