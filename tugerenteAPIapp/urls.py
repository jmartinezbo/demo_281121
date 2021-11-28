from django.urls import path
from .views import ListSaleView
from .views import SaleView
from .views import ListSaleTopView

urlpatterns = [
    path('salesList/', ListSaleView.as_view(), name='salesList'),
    path('salesListTop/<int:top>/', ListSaleTopView.as_view(), name='salesListTop'),
    path('sale/<int:id_item>/', SaleView.as_view(), name='sale'),
]