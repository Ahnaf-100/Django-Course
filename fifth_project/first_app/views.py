from django.shortcuts import render
from . forms import contactForm, Studentdata, PasswordValidatioProject

# Create your views here.
def home(request):
    return render(request, './first_app/home.html')

def about(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        select = request.POST.get("select")
        return render(request,'./first_app/about.html',{'name': name, 'email' : email,'select' : select})
    else:
        return render(request,'./first_app/about.html')

def submit_form(request):
    if request.method == "POST":
        
        name = request.POST.get("username")
        email = request.POST.get("email")
        return render(request,'./first_app/form.html',{'name': name, 'email' : email})
    else:
        return render(request,'./first_app/form.html')
    
def django_form(request):
    if request.method == 'POST':
        form = contactForm(request.POST,request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' +  file.name, 'wb+') as destination :
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            # return render(request, "./first_app/django_forms.html",{"form": form})
        else:
            form = contactForm()
    
    return render(request, "./first_app/django_forms.html",{"form": form})

def student_form(request):
    if request.method == 'POST':
        form = Studentdata(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            form = Studentdata()
    return render(request, "./first_app/django_forms.html",{"form": form})


# def password_form(request):
#     if request.method == 'POST':
#         form = PasswordValidatioProject(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#         else:
#             form = PasswordValidatioProject()
#     return render(request, "./first_app/django_forms.html",{"form" : form})

def password_form(request):
    form = PasswordValidatioProject()  # Move this line outside of the if-else block

    if request.method == 'POST':
        form = PasswordValidatioProject(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        # This part was indented incorrectly in your original code
        form = PasswordValidatioProject()

    return render(request, "./first_app/django_forms.html", {"form": form})
