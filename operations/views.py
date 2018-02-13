from datetime import datetime
from decimal import Decimal

from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from operations.models import *


def operations_list(request):
    if not request.user:
        return redirect(to='error', code='access_denied')

    return render(request, 'operations/operations_list.html')


class BalanceCheckView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(to='index')

        card = request.user

        operation = Operation(type_id=1, card=card, date=datetime.now())
        operation.save()

        return render(request, 'operations/balance_check.html', {
            'card': card,
            'current_date': datetime.now()
        })


class WithdrawView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(to='index')

        return render(request, 'operations/withdraw.html')

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect(to='index')

        card = request.user
        try:
            withdraw_amount = Decimal(request.POST.get('amount'))
        except ValueError:
            return redirect(to='error', code='invalid_input')

        if withdraw_amount > card.balance:
            return redirect(to='error', code='insufficient_funds')

        operation = Operation(type_id=2, card=card, date=datetime.now(), param=withdraw_amount)
        operation.save()

        card.balance -= withdraw_amount
        card.save()

        return render(request, 'operations/withdraw_report.html', {
            'card': card,
            'widthdraw_amount': withdraw_amount,
            'date': operation.date
        })
