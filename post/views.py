from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views.generic.edit import ModelFormMixin

from .forms import PostForm, CommentForm
from .models import Post

# MIXINS HERE

class OwnerMixin(LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('account:profile')
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)


class PostListView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'post/post_list.html'
    context_object_name = "posts"

    def get_queryset(self):
        qs = self.model.objects.all()
        if 'slug' in self.kwargs:
            qs = qs.filter(category__slug=self.kwargs["slug"])
        if 'order' in self.request.GET:
            order = self.request.GET.get('order')
            if order == 'newest':
                qs = qs.order_by("-published")
            else:
                qs = qs.order_by("published")

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'slug' in self.kwargs:
            context['slug'] = self.kwargs['slug']
        

        if 'order' in self.request.GET:
            context['ordering'] = self.request.GET.get('order')

        return context

    #def get_ordering(self):
        
class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm
        context['form'] = form
        return context

class PostCreateView(LoginRequiredMixin,CreateView):
    form_class = PostForm
    success_url = "/annonces/"
    http_method_names = ['post']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

class PostDeleteView(OwnerMixin, DeleteView):
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class PostEditView(OwnerMixin, UpdateView):
    template_name = 'post/post_edit_modal.html'
    form_class = PostForm


# Views for comment
class CommentCreateView(CreateView):
    form_class = CommentForm
    http_method_names = ['post']
    annonce = None

    def dispatch(self, request, *args, **kwargs):
        self.annonce = get_object_or_404(Post, id=self.request.POST.get('id'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.name = self.request.user.username
        form.instance.post = self.annonce
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post:post_detail', args=[self.annonce.slug])

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

