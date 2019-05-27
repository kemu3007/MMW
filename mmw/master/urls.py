from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from master.views import OrderListView

urlpatterns = [
    path(r'', OrderListView.as_view()),
]

