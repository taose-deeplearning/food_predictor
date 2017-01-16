from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render_to_response, render
from django.template import RequestContext
from predictor.models import ImageFile


def index(request):
    return HttpResponse('index')


def upload(request):
    foods =[]

    if request.method == 'POST':
        post_data = request.POST
        post_data.update(request.FILES)
        imagefile = ImageFile()
        image = post_data['image_file']
        if image:
            filename = image['filename']
            imagefile.data = filename
            imagefile.save(filename)

    # json response
    foods.append({'name': u'にんじん'})
    foods.append({'name': u'じゃがいも'})
    return JsonResponse({"foods": foods})


def upload_form(request):
    return render(request, 'upload_form.html')
