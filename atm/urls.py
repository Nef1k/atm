from django.urls import path

from auth_core.views import *

urlpatterns = [
    path('number_input/', NumberInputView.as_view(), name='number_input'),
    path('pin_input/<int:attempt_id>', PinInputView.as_view(), name='pin_input')
]
