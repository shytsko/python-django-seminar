from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from homework3.models import Customer, Product, Order, ProductInOrder
from datetime import datetime, timedelta


class CustomerOrders(TemplateView):
    template_name = "homework3/customer_orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = get_object_or_404(Customer, pk=context['customer_id'])
        orders = customer.orders.all()
        context['customer'] = customer
        context['orders'] = [
            {
                'number': order.pk,
                'date': order.date,
                'total_amount': order.total_amount,
                'products': [
                    {
                        'name': item.product.name,
                        'count': item.product_count,
                        'price': item.product.price,
                        'cost': item.product_count * item.product.price
                    }
                    for item in order.products_in_order.all()],
            }
            for order in orders]
        context['title'] = f'Заказы клиента {customer.name}'
        return context


class CustomerProducts(TemplateView):
    template_name = "homework3/customer_products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = get_object_or_404(Customer, pk=context['customer_id'])
        last_date = datetime.utcnow() - timedelta(days=context['prev_days'])
        products = (ProductInOrder.objects.filter(order__customer=customer, order__date__gte=last_date).
                    order_by('-order__date'))

        context['customer'] = customer
        context['products'] = {product.product for product in products}
        context['title'] = f'Товары клиента'
        return context
