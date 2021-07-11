from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm, massageForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')

	context = {'form': form}
	return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()
	visits = visit.objects.all()
	massages = massage.objects.all()


	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders': orders, 'customers': customers,
			   'total_orders': total_orders, 'delivered': delivered,
			   'pending': pending, 'visits':visits, 'massages':massages}

	return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
	orders = request.user.customer.order_set.all()
	visits = request.user.customer.visit_set.all().order_by('-id')
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	print('ORDERS:', orders)

	context = {'orders': orders, 'total_orders': total_orders,
			   'delivered': delivered, 'pending': pending, 'visits': visits ,  }
	return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES, instance=customer)
		if form.is_valid():
			form.save()

	context = {'form': form}
	return render(request, 'accounts/account_settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
	products = Product.objects.all()

	return render(request, 'accounts/products.html', {'products': products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()
	visits = customer.visit_set.all().order_by('-id')
	vphotos = customer.visit.vphoto_set.all().order_by('-id')
	total_visits = visits.count()

	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs

	context = {'customer': customer, 'orders': orders, 'order_count': order_count,
			   'myFilter': myFilter, 'total_visits':total_visits,'visits':visits , 'vphotos':vphotos}
	return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
	# form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		# print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form': formset}
	return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)
	print('ORDER:', order)
	if request.method == 'POST':

		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form': form}
	return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item': order}
	return render(request, 'accounts/delete.html', context)

def maqals(request):

	maqals = maqal.objects.all().order_by('-id')
	return render(request, 'accounts/maqals.html', {'maqals':maqals})




def Links(request):
	Links = Link.objects.all()
	return render(request, 'accounts/Links.html', {'Links': Links})


def front(request):
	
	form = massageForm()
	if request.method == 'POST':
		# print('Printing POST:', request.POST)
		form = massageForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form': form}


	return render(request, 'accounts/Links.html',  context)

def frist(request):
    context = {}
    return render(request, 'accounts/frist.html', context)


def scond(request):
    context = {}
    return render(request, 'accounts/scond.html', context)


def third(request):
    context = {}
    return render(request, 'accounts/third.html', context)


def f4(request):
    context = {}
    return render(request, 'accounts/fourth.html', context)

def f5(request):
    context = {}
    return render(request, 'accounts/f5.html', context)
def f6(request):
    context = {}
    return render(request, 'accounts/f6.html', context)

def vlog(request):
    vitems = vItem.objects.all()
    return render(request, 'accounts/vlog.html', {'vitems': vitems})




def createmassage(request):
	form = massageForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = massageForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/massage.html', context)




