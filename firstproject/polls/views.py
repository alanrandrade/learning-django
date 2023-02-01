from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def another_view(request):
    return HttpResponse("Hello, world. You're at another view of polls.")