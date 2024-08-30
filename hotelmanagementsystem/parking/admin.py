from django.contrib import admin
from .models import Parkingsections
from .models import Ticketcharges
from .models import Ticket
# Register your models here.

admin.site.register(Parkingsections)
admin.site.register(Ticketcharges)
admin.site.register(Ticket)
