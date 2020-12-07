import json
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .forms import ApplicationForm
from .tasks import send_message, send_message_tg


def main_page(request):
    form = ApplicationForm(request.POST or None)
    if request.is_ajax and request.method == 'POST':
        if form.is_valid():
            quoute = form.save()
            send_message.delay()
            send_message_tg.delay()
            response = {'status': 201, 'message': "Created"}
            return HttpResponse(json.dumps(response), content_type='application/json')
        else:
            response = {'status': 400, 'message': "Invalid data"}
            return HttpResponseBadRequest(json.dumps(response), content_type='application/json')
    return render(request, 'index.html', locals())
