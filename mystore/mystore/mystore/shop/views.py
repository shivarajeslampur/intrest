from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, Order, OrderItem
from .customer import Customer
from .category import Category
from .product import Product
from django.contrib.auth.decorators import login_required

def home(request):
    categories = Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_category_id(categoryID)
    else:
        products = Product.objects.all()
    data = {'products': products, 'categories': categories}
    return render(request, "index.html", data)

def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html")
    else:
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        mobile = request.POST.get('mobile', '')
        password = request.POST.get('password', '')
        #password=make_password(password)
        #storing object
        customerdata=Customer(firstname=firstname,lastname=lastname,email=email,mobile=mobile,password=password)
        uservalues={
            'firstname':firstname,
            'lastname':lastname,
            'email':email,
            'mobile':mobile
        }

        # Validation
        error_msg = None
        success_msg=None

        if not firstname:
            error_msg = "First name should not be empty"
        elif not lastname:
            error_msg = "Last name should not be empty"
        elif not email:
            error_msg = "Email should not be empty"
        elif not mobile:
            error_msg = "Mobile number should not be empty"
        elif not password:
            error_msg = "Password should not be empty"
        elif(customerdata.isexit()):
            error_msg="EMAIL ALREADY EXISTS"
        
        if not error_msg:
            success_msg="Account Created Successfully"
            customerdata.save()
            msg={'success':success_msg}
            return render(request, 'signup.html', msg)
        else:
            msg={'error':error_msg,'value':uservalues}
            return render(request, 'signup.html', msg)

def view_cart(request):
    # Assuming there is a logged-in user
    customer = request.user.customer
    cart, created = Cart.objects.get_or_create(customer=customer)
    cart_items = cart.items.all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    cart_item.delete()
    return redirect('view_cart')

def update_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    cart_item.quantity = quantity
    cart_item.save()
    return redirect('view_cart')

@login_required
def bookNow(request):
    if request.method == 'POST':
        customer = request.user.customer  # Assuming the user is logged in and has a customer profile
        cart = Cart.objects.get(customer=customer)
        cart_items = cart.items.all()

        if not cart_items:
            return redirect('view_cart')

        total = sum(item.product.price * item.quantity for item in cart_items)
        
        order = Order.objects.create(customer=customer, total=total)
        
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Clear the cart
        cart.items.all().delete()

        # Optionally, add a success message or redirect to an order confirmation page
        return redirect('view_cart')
    else:
        return redirect('view_cart')
