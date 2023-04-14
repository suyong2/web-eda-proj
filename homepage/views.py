from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    with open("titanic_EDA.html", "r", encoding='utf-8') as f:
        data = f.read()
    return HttpResponse(data)
