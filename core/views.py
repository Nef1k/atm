from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View


class IndexView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated and request.user.is_active:
            return redirect(to='operations_list')
        else:
            return redirect(to='number_input')


class ErrorView(View):
    errors = {
        'card_doesnt_exists': 'We can\'t find a card with this number',
        'card_blocked': 'Your card has been blocked. Contact administrator',
        'insufficient_funds': 'There\'s not enough money on your balance',
        'attempt_expired': 'You have to start authentication from the begining',
        'pin_invalid': 'Invalid PIN. Return and try again',
        'access_denied': 'You can\'t view this page. Try to sign in first',
        'invalid_input': 'You enter some strange value. That\'s not okey',
    }

    def get(self, request, code):
        error_message = self.errors.get(code)
        return render(request, 'core/error.html', {
            'error_message': error_message
        })