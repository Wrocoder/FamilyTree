from django.contrib import admin

from .models import Person, FamilyRelationship, Family

# Register your models here.
admin.site.register(Family)
admin.site.register(Person)
admin.site.register(FamilyRelationship)