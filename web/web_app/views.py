from django.shortcuts import render
from .models import StatusModel

def index(request, template_name = 'index/index.html'):
    return render(request, template_name)


def status_model_list(request, template_name = 'index/status-model-list.html'):
    title = 'Status Model List'
    status_models = StatusModel.objects.all()
    context = {
        'title' : title,
        'status_models' : status_models,
    }
    return render(request, template_name, context)