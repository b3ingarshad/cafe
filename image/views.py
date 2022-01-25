from django.shortcuts import render
from django.views.generic import ListView
from .models import ImageProfile
from .forms import inputForm
from django.http import HttpResponseRedirect,HttpResponse

class HomePageView(ListView):
    model = ImageProfile
    template_name = 'home.html'

def add(request):     
    form = inputForm(request.POST)     
    if form.is_valid():               
        cd = form.cleaned_data    
        input1 = cd['inputa']
        input2 = cd['inputb']
        output = input1 + input2
        return HttpResponseRedirect('/image/{output}'.format(output=output))
    else:
        form = inputForm()   
    return render(request, 'add/base.html', {'form': form }) 

def thanks(request,id):
    return HttpResponse(f"sum of two numbers will be : {id}")
