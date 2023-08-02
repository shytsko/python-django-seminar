from django.core.management.base import BaseCommand
from homework3.models import Customer, Product, Order
from django.db.models import Max
import random


class Command(BaseCommand):
    help = "Create test data"

    def add_arguments(self, parser):
        parser.add_argument('-d', action='store_true', help='Delete all before')
        parser.add_argument('-c', type=int, help='Count of customers')
        parser.add_argument('-p', type=int, help='Count of products')
        parser.add_argument('-o', type=int, help='Count of orders')

    def handle(self, *args, **kwargs):

        if delete := kwargs.get('d'):
            Customer.objects.all().delete()
            Product.objects.all().delete()

        if count_customers := kwargs.get('c'):
            last_pk = Customer.objects.aggregate(Max("pk"))["pk__max"] or 0
            Customer.objects.bulk_create(
                Customer(
                    name=f"Customer{i}",
                    email=f"customer{i}@mail.com",
                    tel=str(random.randint(1111111111, 9999999999)),
                    address=f"Address of customer{i}",
                )
                for i in range(last_pk + 1, last_pk + count_customers + 1)
            )

        if count_products := kwargs.get('p'):
            last_pk = Product.objects.aggregate(Max("pk"))["pk__max"] or 0
            Product.objects.bulk_create(
                Product(
                    name=f"product{i}",
                    description=f"description of product{i}",
                    price=i % 20 + 1,
                    count=i % 10 + 1
                )
                for i in range(last_pk + 1, last_pk + count_products + 1)
            )

        if count_orders := kwargs.get('o'):
            customers = Customer.objects.all()
            new_orders = Order.objects.bulk_create(
                Order(customer=random.choice(customers)) for _ in range(count_orders)
            )

            products = Product.objects.all()
            for order in new_orders:
                for _ in range(random.randint(5, 10)):
                    order.products.add(random.choice(products),
                                       through_defaults={"product_count": random.randint(1, 5)})
                order.update_total()
