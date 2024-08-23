from django.contrib import admin
from .models import Flan, ContactForm

# Register your models here.

class FlanAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description', 'image_url', 'shortName', 'is_private']


# crear clase contactFormAdmin

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id','customer_email', 'customer_name', 'message']


admin.site.register(Flan, FlanAdmin) 
admin.site.register(ContactForm, ContactFormAdmin) # muestra los detalles de la lista de admin



