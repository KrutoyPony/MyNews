from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Post, Category
from datetime import datetime

# Create your views here.


class PostMany(ListView):
	model = Post
	ordering = '-time_create'
	template_name = 'post_one.html'
	context_object_name = 'post'

class PostAlone(DetailView):
	model = Post
	template_name = 'post_alone.html'
	context_object_name = 'post'


class CategoryMany(ListView):
	model = Category
	ordering = 'name'
	template_name = 'category_many.html'
	context_object_name = 'categoryes'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['time_now'] = datetime.utcnow()
		context['next_sale'] = None
		return context

