from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('orders', views.orders, name="orders"),
    path('returns', views.returns, name="returns"),
    path('cash', views.cash, name="cash"),
    path('insights', views.insights, name="insights"),
    path('inventory', views.inventory, name="inventory"),



    ]

