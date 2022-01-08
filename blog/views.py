from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, 
    CreateView, UpdateView, 
    DeleteView)
from django.contrib.auth.mixins import (
LoginRequiredMixin, UserPassesTestMixin 
)
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    object_list = 'blogs'
    ordering = ['-date']
    login_url = 'login'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    login_url = 'login'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog 
    fields = ['title', 'body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog/blog_update.html'
    fields = ['title', 'body']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog/blog_delete_confirm.html'
    success_url = '/'
    login_url = 'login'


