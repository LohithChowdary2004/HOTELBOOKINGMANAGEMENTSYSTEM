from django.contrib import admin
from .models import Hotels
# Register your models here.
from . models import customer,users
admin.site.register(customer)
admin.site.register(users)

from .models import RoomType

admin.site.register(RoomType)
admin.site.register(Hotels)