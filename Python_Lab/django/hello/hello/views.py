from django.http import HttpResponse

def globalview(request):
    return HttpResponse("first global view")
