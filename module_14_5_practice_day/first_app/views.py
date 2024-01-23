from django.shortcuts import render
from . forms import ExampleForm
# Create your views here.

# def home(request):
#     if request.method == 'POST':
#         form = ExampleForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#         else:
#             form = ExampleForm()

#     return render(request,'home.html', {'form' : form})

def home(request):
    form = ExampleForm()  # Initialize the form outside the if block

    if request.method == 'POST':
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
        # No need for an else block here

    return render(request, 'home.html', {'form': form})
