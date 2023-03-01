from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, ItemForm
from .models import Images
from loguru import logger


def test(request):
    return render(request, './test.html')


def make_one(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)
    if request.method == 'POST':

        postForm = ItemForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
        main_imageForm = ImageForm(request.POST, request.FILES)

        if postForm.is_valid() and formset.is_valid() and main_imageForm.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user

            if post_form.item_type == 'flat':
                post_form.price = int(postForm.cleaned_data[f'{post_form.type}_price'].replace(' ', ''))
                post_form.floor = postForm.cleaned_data['flat_floor']
                post_form.total_floors = postForm.cleaned_data['flat_total_floor']
                post_form.material = postForm.cleaned_data['flat_material']
                post_form.livin_surface = postForm.cleaned_data['flat_livin_surface']

            if post_form.item_type == 'house':
                post_form.price = int(postForm.cleaned_data[f'{post_form.type}_price'].replace(' ', ''))
                post_form.total_floors = postForm.cleaned_data['house_total_floor']
                post_form.material = postForm.cleaned_data['house_material']
                post_form.livin_surface = postForm.cleaned_data['house_livin_surface']

            if post_form.item_type == 'garage':
                post_form.price = int(postForm.cleaned_data[f'{post_form.type}_price'].replace(' ', ''))
                post_form.material = postForm.cleaned_data['garage_material']

            if post_form.item_type == 'com':
                post_form.price = int(postForm.cleaned_data[f'{post_form.type}_price'].replace(' ', ''))
                post_form.floor = postForm.cleaned_data['com_floor']
                post_form.total_floors = postForm.cleaned_data['com_total_floor']
                post_form.material = postForm.cleaned_data['com_material']

            if main_imageForm.cleaned_data['image']:
                main_imageForm = main_imageForm.save(commit=False)
                main_imageForm.post = post_form
                main_imageForm.active = True
                post_form.save()
                main_imageForm.save()
            else:
                post_form.no_pictures = True
                post_form.save()

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

            logger.error(postForm.errors)
            logger.error(formset.errors)
            logger.error(main_imageForm.errors)

    else:
        postForm = ItemForm()
        formset = ImageFormSet(queryset=Images.objects.none())
        main_imageForm = ImageForm()

    return render(request, './create_item_asset/make.html',
                  {'postForm': postForm, 'formset': formset,
                   'main_imageForm': main_imageForm})








