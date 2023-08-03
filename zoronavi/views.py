from django.shortcuts import render,redirect
from django.shortcuts import  render , redirect,get_object_or_404
from zoronavi.forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 

def register(request):	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('zoronavi:login_reg')


	context = { 'form': form }
	return render (request, 'signin/register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('zoronavi:index')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'signin/login.html', context)

def logoutuser(request):
	logout(request)
	return redirect('zoronavi:login_reg')


@login_required(login_url = 'zoronavi:login_reg')
def info(request):
	return render (request,"signin/info.html", context = {})
from django.shortcuts import render

# Create your views here.
def blog_single(request):
    return render(request,'blog_single.html')

def index(request):
    return render(request,'index.html')

def submit(request):
    a = request.POST(['initial'])
    return render(request, 'home/home.html', {
        'error_message': "returned"
    })
