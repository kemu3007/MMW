from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView

from .models import Order, Tag

# Create your views here.


class OrderListView(ListView):
    template_name = 'list.html'
    model = Order
    context_object_name = 'all_post'

    def get_queryset(self):
        results = Order.objects.filter(active=True).order_by('date')
        return results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_category'] = Order.objects.all().order_by('date')
        return context
