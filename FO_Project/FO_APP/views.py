from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Product, CartItem, Payment,Customer
from datetime import datetime
import razorpay
 
def product_list(request):
    products = Product.objects.all()
    return render(request, 'menu.html', {'products': products})
 
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart_item = CartItem.objects.get(product=product)
        # If the item exists, increment the quantity
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        # If the item does not exist, create a new cart item
        cart_item = CartItem(product=product)
        cart_item.save()
    return redirect('menu')
 
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart_item = CartItem.objects.get(product=product)
        # If the item exists, increment the quantity
        cart_item.quantity -= 1
        cart_item.save()
    except CartItem.DoesNotExist:
        # If the item does not exist, create a new cart item
        cart_item = CartItem(product=product)
        cart_item.save()
    return redirect('menu')

# Create your views here.
def index(request):
    username = request.user.username
    return render(request, 'index.html', {'username': username})

def menu(request):
    
    list=Product.objects.all()
    return render(request,'menu.html',{'list':list, })

def reservavtion(request):
    return render(request,'reservation.html',{})

def blog(request):
    return render(request,'blog.html',{})

def blog_detail(request):
    return render(request,'blog-detail.html',{})

def about(request):
    return render(request,'about.html',{})

def login(request):
    return render(request,'login.html',{})

def regs(request):
    return render(request,'regs.html',{})

def contact(request):
    return render(request,'contact.html',{})

def track(request):
    cart_items = CartItem.objects.all()
    item_prices = [int(item.product.price * item.quantity) for item in cart_items]
    total_price = sum(item_prices)
    current_datetime_python = datetime.now()
    # Zip cart_items and item_prices together
    item_data = zip(cart_items, item_prices)
    
    return render(request, 'ot.html', {'item_data': item_data, 'total_price': total_price, 'dt':current_datetime_python})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to index.html or any other page you want to show the user profile
            return redirect('index')
        else:
            # Return an invalid login error message
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login.html')
def regs(request):
    
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phno')    # Assuming 'phno' is the name of the phone number field in your HTML form
        
        # Create a new Customer object and save it to the database
        customer = Customer(username=username, email=email, password=password, phone=phone)
        customer.save()

        # Redirect to a success page or login page
        return redirect('login')  # Replace 'login' with the name of your login URL pattern

    # If request method is not POST, render the registration form
    return render(request,'regs.html',{})

def cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    total_entries = cart_items.count()
    
    if request.method == "POST":
        name = "user"
        amount = total_price
        
        # Create Razorpay order on the server
        client = razorpay.Client(auth=('rzp_test_e7lfhjrd6VffUI', 'mZGsaNcrcHz3A5mNf1MgSFUK'))
        response_payment = client.order.create(dict(amount=amount*100, currency='INR'))
        order_id = response_payment['id']
        order_status = response_payment['status']
        
        if order_status == 'created':
            # Save order details in database
            Payment.objects.create(name=name, amount=amount, order_id=order_id)

            # Pass order details to frontend
            order_details = {
                'id': order_id,
                'amount': amount*100,  # Amount in paise
                'currency': 'INR',
                'name': name,
                'description': 'Food gives you energy',
            }
            return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'total_entries': total_entries, 'order_details': order_details})

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'total_entries': total_entries,})

# def cart(request):
#     cart_items = CartItem.objects.all()
#     total_price = sum(item.product.price * item.quantity for item in cart_items)
#     total_entries = cart_items.count()
#     if request.method == "POST":
#         name = "user"
#         amount = total_price
#         # Create Razorpay client
#         client = razorpay.Client(auth=('rzp_test_e7lfhjrd6VffUI', 'mZGsaNcrcHz3A5mNf1MgSFUK'))

#         # Create order
#         response_payment = client.order.create(dict(amount=amount*100, currency='INR'))
#         order_id = response_payment['id']
#         order_status = response_payment['status']

#         if order_status == 'created':
#             PayDetails = Payment(
#                 name=name,
#                 amount=amount,
#                 order_id=order_id
#             )
#             PayDetails.save()
#             response_payment['name'] = name

#     return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'total_entries': total_entries})

def item(request):
    return render(request, 'item.html')

def additem(request):
    return render(request, 'additem.html')

# def payment(request):
    # if request.method == "POST":
    #     name = "user"
    #     amount = int(request.POST.get('amount')) * 100

    #     # Create Razorpay client
    #     client = razorpay.Client(auth=('rzp_test_e7lfhjrd6VffUI', 'mZGsaNcrcHz3A5mNf1MgSFUK'))

    #     # Create order
    #     response_payment = client.order.create(dict(amount=amount, currency='INR'))
    #     order_id = response_payment['id']
    #     order_status = response_payment['status']

    #     if order_status == 'created':
    #         PayDetails = Payment(
    #             name=name,
    #             amount=amount,
    #             order_id=order_id
    #         )
    #         PayDetails.save()
    #         response_payment['name'] = name

    #         form = CoffeePaymentForm(request.POST or None)
    #         return render(request, 'Coffee_payment.html', {'form': form, 'payment': response_payment})

    # form = CoffeePaymentForm()
    # return render(request, 'Coffee_payment.html', {'form': form})

def payment_status(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    # Client instance   
    client = razorpay.Client(auth=('rzp_test_e7lfhjrd6VffUI', 'mZGsaNcrcHz3A5mNf1MgSFUK'))
    try:
        status = client.utility.verify_payment_signature(params_dict)
        order = order.objects.get(order_id=response['razorpay_order_id'])
        order.razorpay_payment_id = response['razorpay_payment_id']
        order.paid = True
        order.save()
        return render(request, 'payment_status.html', {'status': True})
    except:
        return render(request, 'payment_status.html', {'status': False})
