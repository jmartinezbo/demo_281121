from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=650)
    
    class Meta:
        verbose_name='ProductCategory'
        verbose_name_plural='ProductCategories'

    # def __str__(self):
    #     return self.name

class ProductSubcategory(models.Model):
    name = models.CharField(max_length=650)
    
    class Meta:
        verbose_name='ProductSubcategory'
        verbose_name_plural='ProductSubcategories'

    # def __str__(self):
    #     return self.name


class UnitMeasure(models.Model):
    name = models.CharField(max_length=650)
    
    class Meta:
        verbose_name='UnitMeasure'
        verbose_name_plural='UnitMeasures'

    # def __str__(self):
    #     return self.name
	

class Customer(models.Model):
    name = models.CharField(max_length=650)
    billing_code = models.CharField(max_length=650)
    
    class Meta:
        verbose_name='Customer'
        verbose_name_plural='Customers'

    # def __str__(self):
    #     return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=15)
    
    class Meta:
        verbose_name='PaymentMethod'
        verbose_name_plural='PaymentMethods'

    # def __str__(self):
    #     return self.name


class Product(models.Model):
    sku = models.CharField(default='default', max_length=10, blank=True, null=True)
    name = models.CharField(max_length=650)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='products')
    subcategory = models.ForeignKey(ProductSubcategory, on_delete=models.PROTECT, related_name='products')
    unit_measure = models.ForeignKey(UnitMeasure, on_delete=models.PROTECT, related_name='products')
    
    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'

    # def __str__(self):
    #     return self.name

class Sale(models.Model):
    comment = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, related_name='sales')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='sales')
    
    class Meta:
        verbose_name='Sale'
        verbose_name_plural='Sales'

    # def __str__(self):
    #     return ("{} on {}").format(self.customer, str(self.date))


class SaleDetail(models.Model):
    qty = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=1.0)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=1.0)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='sale_details')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='sale_details')
    
    class Meta:
        verbose_name='SaleDetail'
        verbose_name_plural='SaleDetails'

    # def __str__(self):
    #     return ('{} | Total: {}').format(self.product, self.total)