from django.contrib import admin

from .models import Bicycle,Brand,Color,Order,Transaction, SubOrder,Error
# Register your models here.

admin.site.register(Order)
admin.site.register(SubOrder)


admin.site.register(Bicycle)

admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Transaction)

admin.site.register(Error)