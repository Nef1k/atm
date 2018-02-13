from django.urls import path

from core.views import *
from auth_core.views import *
from operations.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('error/<code>', ErrorView.as_view(), name='error'),

    path('number_input/', NumberInputView.as_view(), name='number_input'),
    path('pin_input/<int:attempt_id>', PinInputView.as_view(), name='pin_input'),
    path('logout/', logout_view, name='logout'),

    path('operations/', operations_list, name='operations_list'),
    path('operations/check', BalanceCheckView.as_view(), name='balance_check'),
    path('operations/widthdraw', WithdrawView.as_view(), name='withdraw'),
]
