from django.shortcuts import render
from django.views.generic import DetailView

from .models import Notebook, Smartphone, Category


def test_view(request):
    categories = Category.object.get_categories_for_left_sidebar()
    context = {
        'categories': categories
    }
    return render(request, 'base.html', context)


class ProductDetailView(DetailView):
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


class CategoryDetailView(DetailView):
    model = Category
    queryset = Category.object.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'
