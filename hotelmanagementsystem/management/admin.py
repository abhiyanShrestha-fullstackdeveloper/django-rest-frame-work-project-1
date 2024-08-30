from django.contrib import admin
from .models import Floor
from .models import Roomtype
from .models import Room
from .models import Empoyee
from .models import Service
# Register your models here.

admin.site.register(Floor)
admin.site.register(Roomtype)
admin.site.register(Room)
admin.site.register(Empoyee)
admin.site.register(Service)
