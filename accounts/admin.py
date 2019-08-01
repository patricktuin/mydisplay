from django.contrib import admin

from accounts.models import Customer
from accounts.models import CustomerDisplaySetting

admin.site.register(Customer)
admin.site.register(CustomerDisplaySetting)
