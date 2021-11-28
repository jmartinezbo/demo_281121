import json

from django.views import View
from django.http import HttpResponse
from django.core import serializers

from .models import Sale
from .models import SaleDetail
from .models import Customer
from .models import PaymentMethod
from .models import Product
from .models import ProductCategory
from .models import ProductSubcategory
from .models import UnitMeasure

from .serializers import SaleSerializer
from .serializers import SaleDetailSerializer
from .serializers import CustomerSerializer
from .serializers import PaymentMethodSerializer
from .serializers import ProductSerializer
from .serializers import ProductCategorySerializer
from .serializers import ProductSubcategorySerializer
from .serializers import UnitMeasureSerializer

# Create your views here.

class SaleView(View):
    def get(self, request, id_item):
        
        res = self.get_sale(id_item)
        return HttpResponse(json.dumps([res]))

    def get_sale(self, id_item):
        obj = Sale.objects.get(pk=id_item)
        res = SaleSerializer(obj).data
        if res:
            res['saledetail'] = self.get_detail(id_item)
            res['customer'] = self.get_customer(res['customer'])
            res['payment_method'] = self.get_payment(res['payment_method'])
        return res

    def get_customer(self, customer_id):
        return CustomerSerializer(Customer.objects.get(pk=customer_id)).data

    def get_payment(self, payment_id):
        return PaymentMethodSerializer(PaymentMethod.objects.get(pk=payment_id)).data

    def get_detail(self, sale_id):
        res = []
        for obj in SaleDetail.objects.filter(sale=sale_id):
            dict_res = SaleDetailSerializer(obj).data
            if dict_res:
                dict_res["product"] = self.get_product(dict_res['product'])
            res.append(dict_res)

        return res

    def get_product(self, product_id):
        res = ProductSerializer(Product.objects.get(pk=product_id)).data
        if res:
            res["category"] = self.get_category(res["category"])
            res["subcategory"] = self.get_subcategory(res["subcategory"])
            res["unit_measure"] = self.get_unitmeasure(res["unit_measure"])
        return res 

    def get_category(self, category_id):
        return ProductCategorySerializer(ProductCategory.objects.get(pk=category_id)).data

    def get_subcategory(self, subcategory_id):
        return ProductSubcategorySerializer(ProductSubcategory.objects.get(pk=subcategory_id)).data
    
    def get_unitmeasure(self, unitmeasure_id):
        return UnitMeasureSerializer(UnitMeasure.objects.get(pk=unitmeasure_id)).data

class ListSaleView(View):
    def get(self, request):
        res = []
        list_obj = Sale.objects.all()
        if list_obj:
            for obj in list_obj:
                res.append(json.loads(SaleView.as_view()(self.request, obj.id).getvalue())[0])
        return HttpResponse(json.dumps(res))

class ListSaleTopView(View):
    def get(self, request, top):
        res = []
        list_obj = Sale.objects.all()[:top]
        if list_obj:
            for obj in list_obj:
                res.append(json.loads(SaleView.as_view()(self.request, obj.id).getvalue())[0])
        return HttpResponse(json.dumps(res))