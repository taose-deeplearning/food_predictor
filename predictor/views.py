from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse, Http404

from django.shortcuts import render
from predictor.models import ImageFile


def index(request):
    return HttpResponse('index')


def upload(request):
    if request.method == 'POST':
        foods = []
        post_data = request.POST
        post_data.update(request.FILES)
        imagefile = ImageFile()
        image = post_data['image_file']
        if image:
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