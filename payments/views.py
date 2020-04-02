import braintree
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order

# api = Api(merchant_id=1396424,
#           secret_key='test')
# checkout = Checkout(api=api)
# data = {
#     "currency": "USD",
#     "amount": 10000
# }
# url = checkout.url(data).get('checkout_url')


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':

        # Получение токена для создания транзакции.
        nonce = request.POST.get('payment_method_nonce', None)
        # Создание и сохранение транзакции.
        total_cost = order.get_total_cost()
        cost_in_grn = float(total_cost) / 24.5
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(cost_in_grn),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            # Отметка заказа как оплаченного.
            order.paid = True
        # Сохранение ID транзакции в заказе.
        # order.braintree_id = result.transaction.id
        order.save()
        return redirect('payment:done')

    else:
        # Формирование одноразового токена для JavaScript SDK.
        client_token = braintree.ClientToken.generate()
        total_cost = order.get_total_cost()
        total_cost = int(total_cost)

        return render(request,
                      'payment/process.html',
                      {'order': order, 'client_token': client_token, 'total_cost': total_cost})


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
