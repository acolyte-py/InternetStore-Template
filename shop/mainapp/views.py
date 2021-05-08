from django.shortcuts import render
from django.views.generic import DetailView, View

from .models import Notebook, Smartphone, Category, LatestProducts
from .mixins import CategoryDetailMixins


class BaseView(View):

    def get(self, request, *args, **kwargs):
        categories = Category.object.get_categories_for_left_sidebar()
        products = LatestProducts.object.get_products_for_main_page(
            'notebook', 'smartphone', with_respect_to='notebook'
        )
        context = {
            'categories': categories,
            'products': products,
        }
        return render(request, 'base.html', context)


class ProductDetailView(CategoryDetailMixins, DetailView):
    CT_MODEL_MODEL_CLASS = {
        'notebook': Notebook,
        'smartphone': Smartphone,
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()

        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'


class CategoryDetailView(CategoryDetailMixins, DetailView):
    model = Category
    queryset = Category.object.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'
