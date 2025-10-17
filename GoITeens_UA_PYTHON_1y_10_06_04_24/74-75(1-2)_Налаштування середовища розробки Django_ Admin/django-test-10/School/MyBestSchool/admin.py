from django.contrib import admin

from .models import Cabinet, Subject, Student

# Register your models here.

admin.site.register([Cabinet, Subject, Student])
