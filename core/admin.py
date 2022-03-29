from django.contrib import admin
from .models import *


class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date']


class ShiftTimeAdmin(admin.ModelAdmin):
    list_display = ['morning', 'afternoon', 'evening', 'shift_started', 'shift_ended']


class ShiftAdmin(admin.ModelAdmin):
    list_display = ['id', 'shift_set', ]


admin.site.register(Worker, WorkerAdmin)
admin.site.register(ShiftTime, ShiftTimeAdmin)
admin.site.register(Shift, ShiftAdmin)
