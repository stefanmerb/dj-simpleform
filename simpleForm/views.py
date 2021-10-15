from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            firstvalue = form.cleaned_data['first_value']
            secondvalue = form.cleaned_data['second_value']
            thirdvalue = form.cleaned_data['third_value']
            result = firstvalue + secondvalue + thirdvalue
            context = {'form': form, 'result' : result}
            return render(request, 'simpleForm/name.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'simpleForm/name.html', {'form': form})