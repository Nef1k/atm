from django.shortcuts import render

# Create your views here.


def number_input(request):
    return render(request, 'auth_core/number_input.html')