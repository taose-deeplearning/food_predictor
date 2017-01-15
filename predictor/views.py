from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.template import RequestContext
from predictor.models import ImageFile


def index(request):
    return HttpResponse('index')


def upload_form(request):
    if request.method == 'POST':
        post_data = request.POST
        post_data.update(request.FILES)
        imagefile = ImageFile()
        image = post_data['image_file']
        if image:
            filename = image['filename']
            imagefile.data = filename
            imagefile.save(filename)