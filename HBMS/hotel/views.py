from audioop import reverse
from random import randint

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
from .form import UserRegisterForm
from django.contrib import messages




from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings

import requests
from django.core.mail import send_mail









def home(request):
    return render(request, 'hotel/home.html')



# def login(request):
#     return render(request, 'hotel/login.html')

def hotels(request):
    return render(request, 'hotel/hotels.html')

def generate_otp():
    return str(randint(100000, 999999))

from django.contrib.auth import login

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .form import UserRegisterForm  # Import your UserRegisterForm
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created Successfully')
            return redirect('send_otp_email')
    else:
        form = UserRegisterForm()
    return render(request, 'hotel/register.html', {'form': form})

otp_storage = {}
def send_otp_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        otp = generate_otp()

        otp_storage[email] = otp

        subject = 'OTP Verification'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        return render(request, 'hotel/validateotp.html', {'otp_sent': True, 'sent_email': email})
    return render(request, 'hotel/send_otp.html')

def validate_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        user_otp = request.POST.get('otp', '')

        stored_otp = otp_storage.get(email)

        if user_otp == stored_otp:
            msg1 = 'OTP validation successful!'
            return render(request, 'hotel/otpvalidation.html',
                          {'msg1': True, 'msg2': False, 'message': msg1, 'mail': email})
        else:
            msg2 = 'Invalid OTP. Please Try Again!'
            return render(request, 'hotel/otpvalidation.html',
                          {'msg1': False, 'msg2': True, 'message': msg2, 'mail': email})

def success_view(request):
    return render(request, 'hotel/success.html')

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def hotel_list(request):
    hotels = [
        {
            'id': 1,
            'name': 'Hotel 1',
            'price_per_room': 100,
            'amenities': ['Free Wi-Fi', 'Pool', 'Restaurant'],
            'max_persons': 2,
            'checkin_date': '2023-10-20',
            'checkout_date': '2023-10-25',
        },
        {
            'id': 2,
            'name': 'Hotel 2',
            'price_per_room': 120,
            'amenities': ['Free Breakfast', 'Gym', 'Spa'],
            'max_persons': 3,
            'checkin_date': '2023-10-22',
            'checkout_date': '2023-10-27',
        },
        {
            'id': 3,
            'name': 'Hotel 3',
            'price_per_room': 100,
            'amenities': ['Free Wi-Fi', 'Pool', 'Restaurant'],
            'max_persons': 2,
            'checkin_date': '2023-10-24',
            'checkout_date': '2023-10-29',
        },
        {
            'id': 4,
            'name': 'Hotel 4',
            'price_per_room': 120,
            'amenities': ['Free Breakfast', 'Gym', 'Spa'],
            'max_persons': 3,
            'checkin_date': '2023-10-26',
            'checkout_date': '2023-10-31',
        },
        {
            'id': 5,
            'name': 'Hotel 5',
            'price_per_room': 100,
            'amenities': ['Free Wi-Fi', 'Pool', 'Restaurant'],
            'max_persons': 2,
            'checkin_date': '2023-10-28',
            'checkout_date': '2023-11-02',
        },
        {
            'id': 6,
            'name': 'Hotel 6',
            'price_per_room': 120,
            'amenities': ['Free Breakfast', 'Gym', 'Spa'],
            'max_persons': 3,
            'checkin_date': '2023-10-30',
            'checkout_date': '2023-11-04',
        },
        # Add more hotels as needed
    ]

    paginator = Paginator(hotels, 4)  # Paginate, showing 4 hotels per page

    page = request.GET.get('page')
    try:
        hotels = paginator.page(page)
    except PageNotAnInteger:
        hotels = paginator.page(1)
    except EmptyPage:
        hotels = paginator.page(paginator.num_pages)

    return render(request, 'hotel/hotels.html', {'hotels': hotels})




def qrcode(request):
    # Replace this with your view logic
    return render(request, 'hotel/contact.html')



from django.shortcuts import render
 # Import your Hotel model here
from datetime import datetime

from datetime import datetime
from django.shortcuts import render
from .models import Hotels
from django.shortcuts import render
from .models import Hotels




from django.shortcuts import render
from .models import Hotels  # Import the Hotel model

from django.shortcuts import render
from .models import Hotels  # Import the Hotel model

# views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Hotels


def hotel_list(request):
    hotels_list = Hotels.objects.all()

    # Add pagination
    paginator = Paginator(hotels_list, 4)
    page = request.GET.get('page')
    hotels = paginator.get_page(page)

    return render(request, 'hotel/hotels.html', {'hotels': hotels})


from django.shortcuts import render, redirect
from .models import Hotels, RoomType


def list_hotels(request):
    hotels = Hotels.objects.all()
    return render(request, 'hotel/list_hotels.html', {'hotels': hotels})


def select_room_type(request, hotel_id):
    hotel = Hotels.objects.get(pk=hotel_id)
    room_types = RoomType.objects.filter(hotel=hotel)
    return render(request, 'hotel/select_room_type.html', {'hotel': hotel, 'room_types': room_types})





from django.shortcuts import render
from .models import Hotels  # Import your Hotel model or whatever you're using to represent hotels

def filter_hotels(request):
    checkin_date = request.GET.get('checkin')
    checkout_date = request.GET.get('checkout')

    # Implement your hotel filtering logic based on check-in and check-out dates
    # For example, you can query your Hotel model to retrieve filtered hotels
    hotels = Hotels.objects.filter(checkin_date__lte=checkin_date, checkout_date__gte=checkout_date)

    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})


from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Hotels  # Import your Hotel model

def calculate_total_price(request):
    if request.method == 'POST':
        hotel_id = request.POST.get('hotel_id')
        num_rooms = int(request.POST.get('num_rooms'))

        # Retrieve the hotel details from the database based on the hotel_id
        hotel = get_object_or_404(Hotels, id=hotel_id)

        # Calculate the total price based on the number of rooms and hotel price
        total_price = num_rooms * hotel.price_per_room  # Calculate the total price here

        # Render the confirmation page with the calculated total price
        context = {
            'hotel': hotel,
            'num_rooms': num_rooms,
            'total_price': total_price,
        }
        return render(request, 'hotel/confirm_booking.html', context)

    return HttpResponse('Method not allowed.')



from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Hotels

from django.shortcuts import render, redirect


def confirm_booking(request, hotel_id, num_rooms, total_price):
    # Convert total_price to a float
    total_price = float(total_price)

    # Retrieve hotel details based on hotel_id (you should implement this logic)
    hotel = Hotels.objects.get(id=hotel_id)

    # Initialize the variables
    checkin_date = None
    checkout_date = None
    total_amount = total_price * num_rooms

    if request.method == 'POST':
        # Handle form submission for check-in and check-out dates
        checkin_date = request.POST.get('checkin_date')
        checkout_date = request.POST.get('checkout_date')

        # Calculate total amount based on total_price, num_rooms, and other factors
        # You can customize this part based on your pricing logic

        # For example, calculating the total amount
        total_amount = total_price * num_rooms

        # You can save booking information to the database here
        # Assuming you have a Booking model for this purpose

    # Render the confirmation page with the booking details
    context = {
        'hotel': hotel,
        'num_rooms': num_rooms,
        'total_price': total_price,
        'checkin_date': checkin_date,
        'checkout_date': checkout_date,
        'total_amount': total_amount,
    }
    return render(request, 'hotel/confirm_booking.html', context)

import razorpay
import json  # Import the 'json' module
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings  # Import Django settings

from .constants import PaymentStatus


from .models import Order
from django.shortcuts import render, HttpResponse
import razorpay
from django.conf import settings
from .models import Order
from django.shortcuts import render, HttpResponse
import razorpay
from django.conf import settings
from .models import Order

from django.shortcuts import render, HttpResponse
import razorpay
from django.conf import settings
from .models import Order

def order_payment(request):
    if request.method == "POST":
        price = request.POST.get("price")
        name = request.POST.get("name")
        email = request.POST.get("email")

        try:
            price = float(price)
        except (ValueError, TypeError):
            return HttpResponse("Invalid price", status=400)

        # Ensure that 'name' is not null and use a default value if it's not provided
        name = name or "Default Name"

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": int(price * 100), "currency": "INR", "payment_capture": 1}
        )
        order = Order.objects.create(
            name=name, amount=price, provider_order_id=razorpay_order["id"]
        )
        order.save()
        return render(
            request,
            "hotel/payment.html",
            {
                "callback_url": "http://127.0.0.1:8000/razorpay/callback/",
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "order": order,
            },
        )

    return render(request, "hotel/booking.html")


from django.http import HttpResponse
from django.shortcuts import render
import razorpay
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Order
from .constants import PaymentStatus

@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if not verify_signature(request.POST):
            order.status = PaymentStatus.SUCCESS
            order.save()
            return render(request, "hotel/callback.html", context={"status": order.status})
        else:
            order.status = PaymentStatus.FAILURE
            order.save()
            return render(request, "hotel/callback.html", context={"status": order.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        return render(request, "hotel/callback.html", context={"status": order.status})


from django.conf import settings

def index(request):
    # Replace this with your view logic
    return render(request, 'hotel/index.html')






# views.py
from django.shortcuts import render, redirect
from .models import hotel_booking  # Import your Booking model


# views.py
from django.shortcuts import render, redirect
 # Import your Booking model

from django.shortcuts import render, redirect
from django.db import transaction
from .models import hotel_booking

@transaction.atomic
def payment(request):
    if request.method == 'POST':
        room_count = request.POST.get('room_count')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        name = request.POST.get('name')
        email = request.POST.get('email')

        # Validate the data as needed
        if room_count and check_in_date and check_out_date and name and email:
            # Create a new Booking instance and save it to the database
            booking = hotel_booking(room_count=room_count, check_in_date=check_in_date, check_out_date=check_out_date, name=name, email=email)
            booking.save()

        # Process the payment here, you can add payment gateway integration code

        # Redirect to a success or failure page based on the payment result


    return render(request, 'payment.html')  # Display the payment page



# views.py
# views.py

from django.shortcuts import render, redirect
from .models import hotel_booking  # Import the Booking model

from django.shortcuts import render, redirect
from .models import hotel_booking  # Import the hotel_booking model

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .models import hotel_booking

from django.shortcuts import render, redirect
from .models import hotel_booking

# views.py
from django.shortcuts import render, redirect



def rooms(request):
    # Replace this with your view logic
    return render(request, 'hotel/rooms.html')


def booking(request):
    # Replace this with your view logic
    return render(request, 'hotel/booking.html')