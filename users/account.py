from django.shortcuts import render
from .models import Favourites
from django.contrib.auth.decorators import login_required
# Create your views here.


def test(request):
    return render(request, './index3.html')


@login_required(login_url='login')
def account(request):
    favourites = Favourites.objects.filter(user=request.user).all()

    params = {
        'favourites': favourites,
    }

    return render(request, './cabinet.html', params)


