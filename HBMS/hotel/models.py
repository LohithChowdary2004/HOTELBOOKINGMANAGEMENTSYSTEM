from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=40,blank=False)
    number=models.IntegerField(max_length=12,blank=False)
    Email=models.CharField(max_length=50,blank=False)

class customer(models.Model):
    name = models.CharField(max_length=40, blank=False)
    number = models.IntegerField(max_length=12, blank=False)
    Email = models.CharField(max_length=50, blank=False)




from django.db import models

class Hotels(models.Model):
    name = models.CharField(max_length=100)
    price_per_room = models.DecimalField(max_digits=10, decimal_places=2)
    amenities = models.TextField()
    max_persons = models.PositiveIntegerField()
    image = models.ImageField(upload_to='hotel_images/')
    rooms=models.IntegerField()

    def __str__(self):
        return self.name



from django.db import models

class RoomType(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=100,
        choices=(
            ('single', 'Single Room'),
            ('double', 'Double Room'),
            ('suite', 'Suite'),
            # Add more predefined room types as needed
        )
    )

    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def get_available_rooms(self, checkin_date, checkout_date):
        # Calculate the number of rooms available based on existing bookings
        existing_bookings = Booking.objects.filter(
            room_type=self,
            checkout_date__gt=checkin_date,
            checkin_date__lt=checkout_date
        )
        total_rooms = self.total_rooms  # Assuming you have a field for total rooms
        available_rooms = total_rooms - existing_bookings.count()
        return available_rooms

    def calculate_total_price(self, num_rooms, checkin_date, checkout_date):
        price_per_night = self.price_per_night
        total_price = price_per_night * num_rooms * (checkout_date - checkin_date).days
        return total_price
    # Add other room type attributes


from django.db import models







from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus

class Order(models.Model):  # Rename 'order' to 'Order'
    name = models.CharField(_("Customer Name"), max_length=254, blank=False, null=False, default="Default Name")  # Set a default value
    amount = models.FloatField(_("Amount"), null=False, blank=False, default=0.0)  # Set a default value
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"),
        max_length=40,
        null=False,
        blank=False,
        default=""
    )

    payment_id = models.CharField(_("Payment ID"), max_length=36, null=False, blank=False,
                                  default="Default Payment ID")  # Set a default value
    signature_id = models.CharField(
        _("Signature ID"),
        max_length=128,
        null=False,
        blank=False,
        default=""
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"


# models.py
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class hotel_booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey to the User model
    name = models.CharField(max_length=100, default=None)
    email = models.CharField(max_length=100, default='NA')
    numbers_of_rooms = models.IntegerField(default=None)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    # Add more fields as needed
    class Meta:
        db_table = 'hotel_booking'
