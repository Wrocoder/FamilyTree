from django.contrib import admin

from .models import Person, FamilyRelationship, Family


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'birth_date', 'photo', 'family_id')
    list_display_links = ('full_name',)
    list_per_page = 10
    search_fields = ('full_name',)


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 10
    search_fields = ('name',)


# Register your models here.
# admin.site.register(Family)
# # admin.site.register(Person)
admin.site.register(FamilyRelationship)
