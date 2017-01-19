# Create your views here.
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from predictor.predictor import get_labels
# from predictor.models import ImageFile


def index(request):
    return HttpResponse('index')


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        foods = []
        post_data = request.POST
        post_data.update(request.FILES)
        # imagefile = ImageFile()
        image = post_data['image_file']
        if image:
            # imagefile.data = image
            # for debug
            array = get_labels(image)
            for ar in array:
                foods.append({'name': ar})
        return JsonResponse({"foods": foods})
    else:
        raise Http404('invalid request')


def upload_form(request):
    return render(request, 'upload_form.html')
