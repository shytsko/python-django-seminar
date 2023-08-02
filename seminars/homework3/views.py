from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from homework3.models import Customer, Product, Order


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
