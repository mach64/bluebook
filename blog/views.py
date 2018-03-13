# from django.shortcuts import render
from django.views.generic import DetailView, ListView, View
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Tag, Profile
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class PostList(ArchiveIndexView):
    """List of recent posts."""
    model = Post
    date_field = 'pub_date'
    template_name = 'blog/post_list.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'tags', 'author']


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'tags']


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')


class TagDetail(ListView):
    template_name = 'blog/tag_detail.html'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, name=self.kwargs['tag_name'])
        return self.tag.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs['tag_name']
        return context


class AccountProfile(DetailView):
    template_name = 'account/account_profile.html'

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)


class UserProfile(DetailView):
    model = Profile
    template_name = 'blog/profile.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['uname'])
