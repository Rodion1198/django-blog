from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.decorators.cache import cache_page

from .forms import CommentForm, EditForm, FeedbackForm, PostForm
from .models import Category, Comment, Post, RSSPost


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('article-detail', args=[pk]))


def category_list_view(request):
    category_list_menu = Category.objects.all()
    return render(request, 'category_list.html', {'category_list_menu': category_list_menu})


@cache_page(10)
def category_view(request, category):
    category_posts = Post.objects.filter(category=category).order_by('-post_date')
    return render(request, 'categories.html', {'category': category.title(),
                                               'category_posts': category_posts})


def feedback_form(request):
    if request.method == 'GET':
        form = FeedbackForm()
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            subject = 'New Feedback!!'
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(subject, message, from_email, ['admin@example.com'])

            return redirect('home')
    return render(request, 'contact.html', context={'form': form})


class HomeView(generic.ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context


class ArticleDetailView(generic.DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(**kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        count_likes = stuff.count_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['category_menu'] = category_menu
        context['count_likes'] = count_likes
        context['liked'] = liked
        return context


class AddPostView(SuccessMessageMixin, generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_message = 'Post created'


class AddCommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class AddCategoryView(SuccessMessageMixin, generic.CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    success_message = 'Category added'


class UpdatePostView(SuccessMessageMixin, generic.UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    success_message = 'Post updated'


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class RSSPostList(generic.ListView):
    model = RSSPost
    template_name = 'rss_post_list_page.html'
    paginate_by = 10
