from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from ..form import AddForm
from django.contrib import messages
from handlers.models import BlackList
# Create your views here.


@permission_required('handlers.control_black_list', login_url='login')
def extended_black_list(request):
    black_list = BlackList.objects.all()
    return render(request, './advanced_admin/extend_black_list/extended_black_list.html', {'black_list': black_list})


@permission_required('handlers.control_black_list', login_url='login')
def extended_black_list_page(request, phone_id):
    number = BlackList.objects.get(id=phone_id)
    if request.method == 'POST':

        if request.POST['action'] == 'Удалить номер телефона':
            number.delete()
            messages.info(request, 'Номер удален из черного списка')
            return redirect('extended_black_list')

    return render(request, './advanced_admin/extend_black_list/extended_black_list_page.html', {'number': number})


@permission_required('handlers.control_black_list', login_url='login')
def extended_black_list_add(request):

    if request.method == 'POST':
        if request.POST['action'] == 'Добавить':
            form = AddForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Телефон успешно добавлен')
                return redirect('extended_black_list')

    else:
        form = AddForm()
    return render(request, './advanced_admin/extend_black_list/extended_black_list_add.html',
                  {'form': form})
