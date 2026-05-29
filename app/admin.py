from django.contrib import admin 
from app.models import Profile,serviceprovider,Servicebooking,Payment

admin.site.register(Profile)
admin.site.register(serviceprovider)
admin.site.register(Servicebooking)
admin.site.register(Payment)

