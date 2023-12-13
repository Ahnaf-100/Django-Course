from django.http import HttpResponse


def home(request):
    return HttpResponse("This is homepage")

def blank(request):
    return HttpResponse("this is blank page")