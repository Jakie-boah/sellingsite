from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, ItemForm
from .models import Images
from loguru import logger


def make_one(request):
    # extra_questions = get_questions(request)
    # ItemFormSet = formset_factory(ItemForm, extra=0)

    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)
    # 'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        postForm = ItemForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,)

        if request.method == 'POST':

            postForm = ItemForm(request.POST)
            formset = ImageFormSet(request.POST, request.FILES,
                                   queryset=Images.objects.none())

            if postForm.is_valid() and formset.is_valid():
                post_form = postForm.save(commit=False)
                post_form.user = request.user

                logger.info(post_form.item_type)
                if post_form.item_type == 'flat':
                    post_form.floor = postForm.cleaned_data['flat_floor']
                    post_form.material = postForm.cleaned_data['flat_material']
                    post_form.livin_surface = postForm.cleaned_data['flat_livin_surface']

                if post_form.item_type == 'house':
                    post_form.total_floors = postForm.cleaned_data['house_total_floor']
                    post_form.material = postForm.cleaned_data['house_material']
                    post_form.livin_surface = postForm.cleaned_data['house_livin_surface']

                if post_form.item_type == 'garage':
                    post_form.material = postForm.cleaned_data['garage_material']

                if post_form.item_type == 'com':
                    post_form.floor = postForm.cleaned_data['com_floor']
                    post_form.total_floors = postForm.cleaned_data['com_total_floor']
                    post_form.material = postForm.cleaned_data['com_material']

                post_form.save()
                koll = 0
                for form in formset.cleaned_data:
                    # this helps to not crash if the user
                    # do not upload all the photos
                    if form:
                        image = form['image']
                        if koll == 0:
                            photo = Images(post=post_form, image=image, active=True)
                            koll += 1
                        else:
                            photo = Images(post=post_form, image=image)

                        photo.save()
                # use django messages framework
                messages.success(request,
                                 "Yeeew, check it out on the home page!")
                return HttpResponseRedirect("/")
            else:
                print(postForm.errors, formset.errors)
    else:
        postForm = ItemForm(request.POST, initial={'item_type': 1})
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, './make.html',
                  {'postForm': postForm, 'formset': formset})









