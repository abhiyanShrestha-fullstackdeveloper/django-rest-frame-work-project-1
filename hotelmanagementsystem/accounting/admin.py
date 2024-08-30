from django.contrib import admin
from .models import Bills
from .models import Payment
from .models import Employeesalary
# Register your models here.

admin.site.register(Bills)
admin.site.register(Payment)
admin.site.register(Employeesalary)