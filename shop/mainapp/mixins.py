from django.views.generic.detail import SingleObjectMixin

from .models import Category
    

class CategoryDetailMixins(SingleObjectMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = (
            Category.object.get_categories_for_left_sidebar()
        )
        return context
