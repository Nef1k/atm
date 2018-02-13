from datetime import datetime

from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from auth_core.models import Card, AuthAttempt


class NumberInputView(View):
    def get(self, request):
        return render(request, 'auth_core/number_input.html')

    # TODO: Make a form from this
    def post(self, request: HttpRequest):
        card_number = request.POST.get('card_number', 'invalid_number')

        # TODO: Redirect to error page (card does not exists)
        card = get_object_or_404(Card, pk=card_number)

        if not card.is_active:
            # TODO: Redirect to error page (card blocked)
            pass

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
            # TODO: Redirect to error page (card blocked)
            pass

        pin = request.POST.get('pin', 'invalid_pin')

        if card.pin == pin:
            if not card.auth_attempts_failed == 0:
                card.auth_attempts_failed = 0
                card.save()

            attempt.delete()
            login(request, card)
            # TODO: Redirect to operations page
        else:
            card.auth_attempts_failed += 1
            if card.auth_attempts_failed >= 4:
                card.is_active = False
                attempt.delete()
            card.save()

            return redirect('pin_input', attempt_id=attempt_id)

        return HttpResponse('Hello, world!')
