from django.contrib import admin

from .models import ProductCategory
from .models import ProductSubcategory
from .models import UnitMeasure
from .models import Customer
from .models import PaymentMethod
from .models import Product
from .models import Sale
from .models import SaleDetail

# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

class ProductSubcategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

class UnitMeasureAdmin(admin.ModelAdmin):
    list_display = ("name",)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name","billing_code")

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ("name",)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("sku", "name", "category", "subcategory", "unit_measure", )

class SaleDetailAdminInline(admin.TabularInline):
    model = SaleDetail

class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "date", "payment_method", "discount", "amount", )
    inlines = (SaleDetailAdminInline, )


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductSubcategory, ProductSubcategoryAdmin)
admin.site.register(UnitMeasure, UnitMeasureAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)