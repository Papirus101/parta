from django.contrib import admin

from .models import Classes, Teacher, Lessons, Tariff, Cart, Products


admin.site.register(Classes)
admin.site.register(Teacher)
admin.site.register(Lessons)
admin.site.register(Tariff)
admin.site.register(Cart)
admin.site.register(Products)
