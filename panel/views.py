# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db import models
from django.http import HttpResponseRedirect

from product.models import Product, Category
from .forms import ProductForm

class ProductCreate(generic.View):
	def get(self, request, *args, **kwargs):
		context = {
		'form':ProductForm()
		}
		return render(request, 'product/create.html', context)

	def post(self, request, *args, **kwargs):
		form = ProductForm(request.POST, request.FILES)		
		if form.is_valid():
			product = form.save(commit=False)			
			product.save()
			return HttpResponseRedirect('/')
		context = {'form':form}
		return render(request, 'product/create.html', context)


product_create = ProductCreate.as_view()


