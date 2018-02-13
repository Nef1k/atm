from django.urls import path

from core.views import *
from auth_core.views import *

urlpatterns = [
    path('error/<code>', ErrorView.as_view(), name='error'),

    path('number_input/', NumberInputView.as_view(), name='number_input'),
    path('pin_input/<int:attempt_id>', PinInputView.as_view(), name='pin_input')
]
