from django.contrib import admin

from .models import Flat, Claim, Owner


class OwnersInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address', 'id')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'id')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [OwnersInline]


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ('full_name',)

