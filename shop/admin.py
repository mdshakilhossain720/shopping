from django.contrib import admin
from.models import Contractmodel
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=['id','full_name','email','subject','description']

admin.site.register(Contractmodel,ContactAdmin)

