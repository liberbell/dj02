from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Pet

# Create your views here.
def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})
    return HttpResponse('<p>home view</p>')

def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    # return HttpResponse('<p>detail view with the id {}</p>'.format(id))

    return render(request, 'pet_detail.html', {'pet': pet})
