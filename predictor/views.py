from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
from django.http import HttpResponse, JsonResponse, Http404

from django.shortcuts import render
=======
from django.http import HttpResponse

from django.shortcuts import render_to_response
>>>>>>> f4dbfcf... [WIP] upload images
from django.template import RequestContext
from predictor.models import ImageFile


def index(request):
    return HttpResponse('index')


<<<<<<< HEAD
def upload(request):
    if request.method == 'POST':
        foods = []
=======
def upload_form(request):
    if request.method == 'POST':
>>>>>>> f4dbfcf... [WIP] upload images
        post_data = request.POST
        post_data.update(request.FILES)
        imagefile = ImageFile()
        image = post_data['image_file']
        if image:
<<<<<<< HEAD
            imagefile.data = image
            # for debug
            foods.append({'name': u'パイナップル'})

        # json response
        # for debug
        foods.append({'name': u'りんご'})
        return JsonResponse({"foods": foods})
    else:
        raise Http404('invalid request')


def upload_form(request):
    return render(request, 'upload_form.html')
=======
            filename = image['filename']
            imagefile.data = filename
            imagefile.save(filename)
>>>>>>> f4dbfcf... [WIP] upload images
