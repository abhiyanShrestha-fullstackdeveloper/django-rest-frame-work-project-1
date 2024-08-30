from django.contrib import admin
from .models import Foodcategory
from .models import Food
from .models import Order
from .models import Table
from .models import Menu
from .models import Resturantbill
# Register your models here.

admin.site.register(Foodcategory)
admin.site.register(Food)
admin.site.register(Order)
admin.site.register(Table)
admin.site.register(Menu)
admin.site.register(Resturantbill)
