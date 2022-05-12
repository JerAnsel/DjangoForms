from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import FlavorForm


def formRender(request):
    context = {} 

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FlavorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data as required
            # ...
            # return some response:
            return HttpResponse("Thanks for your data!")
        
        # If the form was invalid send the user back to fix it
        else:
            return render(request, 'formyapp/formPage.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FlavorForm()
        context['form'] = form

    return render(request, 'formyapp/formPage.html', context)
