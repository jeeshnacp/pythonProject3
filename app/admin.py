from django.contrib import admin

# Register your models here.
from app.models import Login, hospital, nurse

admin.site.register(Login)
admin.site.register(hospital)
admin.site.register(nurse)
# admin.site.register(customer)
# admin.site.register(reportcard)
# admin.site.register(Schedule)
# admin.site.register(vaccine)
# admin.site.register(appointment)
# admin.site.register(complaints)
