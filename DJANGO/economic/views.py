from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView


from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    content = {
        "title" : "Home Page",
        "content" : "Welcome to Home Page"
    }
    return render(request, "home_page.html", content)
def about_page(request):
    content = {
        "title" : "About Page",
        "content" : "Welcome to About Page"
    }
    return render(request, "home_page.html", content)
def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    content = {
        "title" : "Contact Page",
        "content" : "Welcome to Contact Page",
        "form" : contact_form
    }

    if contact_form.is_valid():              # kiem tra email co hop le hay khong
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    return render(request, "contact/view.html", content)


User = get_user_model()

def login_page(request):
    login_template = LoginForm(request.POST or None)
    content = {
        "title" : "Login Page",
        "form": login_template
    }
    if login_template.is_valid():
        # print(login_template.cleaned_data)
        username = login_template.cleaned_data.get("username")      # lay username da duoc luu vao cleaned_data
        password = login_template.cleaned_data.get("password")      # lay password da duoc luu vao cleaned_data
        user = authenticate(username=username, password=password)   # tao ket noi thanh cong username va password


        if user is not None:
            # login_template = LoginForm(request.POST or None)
            login(request, user)                                    # login thanh cong
            print("Dang nhap thanh cong")
            return redirect("/")
        else:
            print("ERROR::NOCREATE")

    return render(request, 'auth/login.html', content)

def logout_view(request):
    logout(request)
    return redirect('/')

def register_page(request):
    register_template = RegisterForm(request.POST or None)
    content = {
        'title' : 'RegisterForm',
        'form' : register_template
    }
    if register_template.is_valid():
        register_template.cleaned_data
        username = register_template.cleaned_data.get("username")
        email    = register_template.cleaned_data.get("email")
        password = register_template.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)

        # print(new_user)

    return render(request, "auth/register.html", content)
