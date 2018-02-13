from django.shortcuts import render
from django.views import View


class ErrorView(View):
    errors = {
        'card_doesnt_exists': 'We can\'t find a card with this number',
        'card_blocked': 'Your card has been blocked. Contact administrator',
        'insufficient_funds': 'There\'s not enough money on your balance',
        'pin_invalid': 'Invalid PIN. Return and try again'
    }

    def get(self, request, code):
        error_message = self.errors.get(code, None)
        return render(request, 'core/error.html', {
            'error_message': error_message
        })