from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, ItemForm
from .models import Images
from loguru import logger


def test(request):
    return render(request, './index3.html')

def make_one(request):

    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)
    if request.method == 'POST':

        postForm = ItemForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)
        main_imageForm = ImageForm(request.POST)

        if request.method == 'POST':

            postForm = ItemForm(request.POST)
            formset = ImageFormSet(request.POST, request.FILES,
                                   queryset=Images.objects.none())
            main_imageForm = ImageForm(request.POST, request.FILES)

            if postForm.is_valid() and formset.is_valid() and main_imageForm.is_valid():
                post_form = postForm.save(commit=False)
                post_form.user = request.user
                main_imageForm = main_imageForm.save(commit=False)

                logger.info(post_form.item_type)

                if post_form.item_type == 'flat':
                    post_form.price = postForm.cleaned_data[f'{post_form.type}_price']
                    post_form.floor = postForm.cleaned_data['flat_floor']
                    post_form.material = postForm.cleaned_data['flat_material']
                    post_form.livin_surface = postForm.cleaned_data['flat_livin_surface']

                if post_form.item_type == 'house':
                    post_form.price = postForm.cleaned_data[f'{post_form.type}_price']
                    post_form.total_floors = postForm.cleaned_data['house_total_floor']
                    post_form.material = postForm.cleaned_data['house_material']
                    post_form.livin_surface = postForm.cleaned_data['house_livin_surface']

                if post_form.item_type == 'garage':
                    post_form.price = postForm.cleaned_data[f'{post_form.type}_price']
                    post_form.material = postForm.cleaned_data['garage_material']

                if post_form.item_type == 'com':
                    post_form.price = postForm.cleaned_data[f'{post_form.type}_price']
                    post_form.floor = postForm.cleaned_data['com_floor']
                    post_form.total_floors = postForm.cleaned_data['com_total_floor']
                    post_form.material = postForm.cleaned_data['com_material']

                post_form.save()
                main_imageForm.post = post_form
                main_imageForm.active = True
                main_imageForm.save()
                for form in formset.cleaned_data:

                    if form:
                        image = form['image']
                        photo = Images(post=post_form, image=image)

                        photo.save()

                messages.success(request,
                                 "Объявление создано. Отправлено модератору на подтверждение.")

                # send_message() будет отправлять уведомление о создании нового объявления

                return HttpResponseRedirect("/")
            else:
                print(postForm.errors, formset.errors)
    else:
        postForm = ItemForm(request.POST, initial={'item_type': 1})
        formset = ImageFormSet(queryset=Images.objects.none())
        main_imageForm = ImageForm(request.POST)

    return render(request, './make.html',
                  {'postForm': postForm, 'formset': formset,
                   'main_imageForm': main_imageForm})









