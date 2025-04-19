# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a page created by Kiran for collabaration Project.")