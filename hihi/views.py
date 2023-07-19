from django.shortcuts import render
from .models import People
from django.utils import timezone


# Create your views here.
def post_list(request):
    posts = People.objects.filter(time_publish__lte=timezone.now()).order_by('time_publish')
    return render(request, 'hihi/post_list.html', {'posts': posts})
