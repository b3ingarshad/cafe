from django.contrib import admin
from .models import Member, Product,category,tab,time,Order


# Register your models here.
admin.site.register(Product)
admin.site.register(Member)
admin.site.register(category)
admin.site.register(tab)
admin.site.register(time)
admin.site.register(Order)