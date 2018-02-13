from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from auth_core.models import Card, AuthAttempt


def logout_view(request):
    logout(request)
    return redirect(to='index')


class NumberInputView(View):
    def get(self, request):
        return render(request, 'auth_core/number_input.html')

    # TODO: Make a form from this
    def post(self, request):
        try:
            card_number = int(request.POST.get('card_number', 'invalid_number'))
        except ValueError:
            return redirect('error', code='invalid_input')

        try:
            card = Card.objects.get(pk=card_number)
        except Card.DoesNotExist:
            return redirect(to='error', code='card_doesnt_exists')

        if not card.is_active:
            return redirect(to='error', code='card_blocked')

        auth_attempt = AuthAttempt()
        auth_attempt.card = card
        auth_attempt.attempt_date = datetime.now()
        auth_attempt.save()

        return redirect(to='pin_input', attempt_id=auth_attempt.pk)


class PinInputView(View):
    def get(self, request, attempt_id):
        return render(request, 'auth_core/pin_input.html', {
            'attempt_id': attempt_id
        })

    def post(self, request, attempt_id):
        # Lol what
        attempt = get_object_or_404(AuthAttempt, pk=attempt_id)

        card = attempt.card
        if not card.is_active:
            return redirect(to='error', code='card_blocked')

        try:
            pin = int(request.POST.get('pin', 'invalid_pin'))
        except ValueError:
            return redirect('error', code='invalid_input')

        if not card.pin == pin:
            card.auth_attempts_failed += 1
            if card.auth_attempts_failed >= 4:
                card.is_active = False
                attempt.delete()
            card.save()
            return redirect(to='error', code='pin_invalid')

        # Success
        if not card.auth_attempts_failed == 0:
            card.auth_attempts_failed = 0
            card.save()
        attempt.delete()
        login(request, card)
        return redirect(to='operations_list')
