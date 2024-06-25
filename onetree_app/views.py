from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
    return render(request,'index.html')


def menu(request):
    return render(request,'menu.html')

def dashboard(request):
    return render(request,'dashboard.html')


def loginpage(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        #authenticating the user with the username and password
        user=authenticate(request,username=username,password=password)
      

        if user is not None:
                login(request,user)
                return redirect('home.html')
        else:
            messages.info(request,'Username or Password doesnt exist!!')


        #check if the login form is valid or not
    return render(request,'login.html')

def signuppage(request):
    form=SignupForm()   #initialized the user creation form object and stored in the form variable
    #handling the input submit request
    if request.method=='POST':
        #populate the empty user creation form
        form=SignupForm(request.POST) 

        #check if the populated user creation form is valid
        if form.is_valid():
            user=form.cleaned_data.get('username')
            form.save()
            messages.success(request,'Account created Successfully for'+" " +user)
            return redirect('login')

    context={"form":form}
    return render(request,'signup.html',context)




