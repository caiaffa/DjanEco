# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db import models
from django.views.decorators.cache import cache_page


from .models import Product, Category


class ProductList(generic.ListView):

    template_name = 'product/product_list.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        queryset = Product.objects.all()
        #q = self.request.GET.get('q', '')
        #if q:
        #    queryset = watson.filter(queryset, q)
        return queryset


product_list = ProductList.as_view()


class CategoryList(generic.ListView):

    template_name = 'product/category.html'
    context_object_name = 'product_list'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


category = CategoryList.as_view()


@cache_page(60 * 10)
def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'product/product.html', context)
