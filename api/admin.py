# Register your models here.
from django.contrib import admin

from api.models import Relationship, Person

admin.site.register(Person)
admin.site.register(Relationship)
