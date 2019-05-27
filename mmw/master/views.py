from django.views.generic import ListView

from .models import Order, Tag

# Create your views here.


class OrderListView(ListView):
    template_name = 'index.html'
    model = Order
    context_object_name = 'all_order'

    def get_queryset(self):
        results = Order.objects.filter(active=True).order_by('-date')
        return results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_order'] = Order.objects.all().order_by('-date')
        context['calc_sum'] = Order.calc_sum()['money__sum']
        context['all_tag'] = Tag.objects.all()
        return context
