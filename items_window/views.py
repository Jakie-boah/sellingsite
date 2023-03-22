from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, ItemForm
from .models import Images
from loguru import logger
from create_item_handler.post_handler import Post, PostMainImage, PostImages


def make_one(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)
    if request.method == 'POST':

        postForm = ItemForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())
        main_imageForm = ImageForm(request.POST, request.FILES)

        if postForm.is_valid() and formset.is_valid() and main_imageForm.is_valid():
            post_form = postForm.save(commit=False)

            # Создание объявления
            new_post = Post(post_form.item_type, post_form, postForm)
            current_type = new_post.get_item_class()
            current_type.create()

            # Установка основного изображения
            main_image = PostMainImage(main_imageForm, post_form)
            main_image.set_main_image()

            # Установка остальных изображений
            setup = PostImages(formset.cleaned_data, post_form)
            setup.set_rest_images()

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








