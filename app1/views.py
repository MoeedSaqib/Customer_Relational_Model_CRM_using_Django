from django.shortcuts import render , redirect

from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import*
from .filters import*
from django.contrib import messages
from .decoraters import *


@unauthenticated_user 
def registerPage(request):

        form=CreateUserForm()

        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                username =form.cleaned_data.get('username')
                group=Group.objects.get(name='customers')
                user.groups.add(group)

                customer.objects.create(user=user,)
               
                messages.success(request, 'Account was created for '+ username )



                return redirect('login')
        context={'form':form}
        return render(request,'app1/register.html', context)    

@unauthenticated_user            
def loginPage(request):
  
    if request.method =="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username Or Password is Inncorrect')


    context={}
    return render(request,'app1/login.html', context)    



def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    orders = Orders.objects.all()
    customers = customer.objects.all()
    total_customers=customers.count()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()
    context= {'orders':orders , 'customers':customers ,'total_orders':total_orders,
              'total_customers':total_customers,
              'delivered':delivered, 'pending':pending} 
    return render(request,'app1/home.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def userPage(request):
     orders = request.user.customer.orders_set.all()

     total_orders=orders.count()
     delivered=orders.filter(status='Delivered').count()
     pending=orders.filter(status='Pending').count()

     context={'orders':orders ,'total_orders':total_orders,'delivered':delivered, 'pending':pending}
     return render(request , 'app1/user.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['customers'])
def accountSettings(request):
    customer=request.user.customer
    form=CustomerForm(instance=customer)
     
    if request.method=="POST":
      form=CustomerForm(request.POST , request.FILES,instance=customer)
      if form.is_valid():
          form.save()

    context={'form':form }
    return render(request , 'app1/account_settings.html', context)
    

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def products(request):
    products = Product.objects.all()
    return render( request,'app1/products.html' , {'list_of_products':products} )

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def customers(request , pk_test):
    customers=customer.objects.get(id=pk_test)

    orders=customers.orders_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET , queryset=orders)

    orders=myFilter.qs  
    context={'customers':customers , 'orders':orders , 'myFilter':myFilter,'order_count':order_count}
    return render(request,'app1/customers.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])


def createOrder(request,pk):
    OrderFormSet=inlineformset_factory(customer, Orders , fields=('product', 'status') , extra=10)
    customers = customer.objects.get(id=pk)
    formset = OrderFormSet(instance=customers)
   # form=OrderForm #(initial={'customer':customers})
    if request.method == 'POST':
        #form=OrderForm(request.POST)
        formset = OrderFormSet(request.POST ,instance=customers)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset }
    return  render(request ,'app1/order_form.html', context )


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])

def updateOrder(request ,pk ):
    order = Orders.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method == 'POST':
        form=OrderForm(request.POST , instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return  render(request ,'app1/order_form.html', context )


@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def deleteOrder(request ,pk ):

    order = Orders.objects.get(id=pk)
    if request.method == "POST":
        order.delete()

        return redirect('/')
    context = {'item':order}
    return  render(request ,'app1/delete.html', context )
