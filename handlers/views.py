from django.shortcuts import render, redirect
from .form import FeedBackForm
from django.contrib import messages
from loguru import logger
# Create your views here.


def contacts(request):
    if request.method == 'POST':

        form = FeedBackForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request,
                             "Спасибо за Вашу обратную связь!")
            return redirect('index')

        else:
            logger.error(form.errors)
    else:
        form = FeedBackForm()

    return render(request, './contact.html', {'form': form})
