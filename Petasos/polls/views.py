from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Index page response.
    """
    return HttpResponse("Hello world")
