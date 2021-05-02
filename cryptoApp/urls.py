from django.urls import path     
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("prices/", views.prices, name="prices" ),
    path("moneyTime/", views.moneyMaker, name="priceDif"),
    path("lookup/", views.lookup, name="lookup")
]