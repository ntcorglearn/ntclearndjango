from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, I am at Devops Training. Amrit Nepal")
