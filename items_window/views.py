from django.shortcuts import render
from django.forms import modelformset_factory, formset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, ItemForm
from .models import Images
from loguru import logger


def post(request):
    #extra_questions = get_questions(request)
    # ItemFormSet = formset_factory(ItemForm, extra=0)

    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    # 'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        postForm = ItemForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,)

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.type = postForm.cleaned_data['type']
            post_form.item_type = postForm.cleaned_data['item_type']
            logger.info(post_form.item_type)
            if post_form.item_type == 'land' or post_form.item_type == 'carplace':
                post_form.total_surface = postForm.cleaned_data['total_surface']
                post_form.save()
                logger.info(formset.cleaned_data)
                for form in formset.cleaned_data:
                    logger.info(form)
                    # this helps to not crash if the user
                    # do not upload all the photos
                    if form:
                        image = form['image']
                        photo = Images(post=post_form, image=image)
                        photo.save()
                # use django messages framework
                logger.success(
                    "Yeeew, check it out on the home page!")
                return HttpResponseRedirect("/")
            else:

                post_form.floor = postForm.cleaned_data[f'{post_form.item_type}_floor']
                if post_form.item_type == 'house' or post_form.item_type == 'com':
                    post_form.total_floor = postForm.cleaned_data[f'{post_form.item_type}_total_floor']
                post_form.material = postForm.cleaned_data[f'{post_form.item_type}_material']
                post_form.total_surface = postForm.cleaned_data['total_surface']
                post_form.livin_surface = postForm.cleaned_data[f'{post_form.item_type}_livin_surface']
                post_form.price = postForm.cleaned_data[f'price']
                post_form.trade = postForm.cleaned_data[f'trade']
                post_form.description = postForm.cleaned_data[f'description']
                post_form.save()
                logger.info(formset.cleaned_data)
                for form in formset.cleaned_data:
                    logger.info(form)
                    # this helps to not crash if the user
                    # do not upload all the photos
                    if form:
                        image = form['image']
                        photo = Images(post=post_form, image=image)
                        photo.save()
                # use django messages framework
                logger.success(
                    "Yeeew, check it out on the home page!")
                return HttpResponseRedirect("/")

        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = ItemForm(request.POST, initial={'item_type': 1})
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, './test_form.html',
                  {'postForm': postForm, 'formset': formset})




# we'll dynamically create the elements, no need for any forms

def post1(request):
    ItemFormSet = formset_factory(ItemForm, extra=0)

    if request.method == "POST":
        formset = ItemFormSet(request.POST)
        for form in formset.forms:
            pass
            #print "You've picked {0}".format(form.cleaned_data['color'])
    else:
        formset = ItemFormSet()
    return render(request, './test_form1.html', {'formset': formset})



def test(request):
    return render(request, './sample.html')







