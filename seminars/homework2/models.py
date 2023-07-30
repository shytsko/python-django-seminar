from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    tel = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Customer({self.pk}: {self.name})"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product({self.pk}: {self.name})"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order({self.pk}: Customer - {self.customer.name}; Products - {self.products})"
