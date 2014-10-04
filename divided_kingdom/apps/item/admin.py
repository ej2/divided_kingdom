from django.contrib import admin
from divided_kingdom.apps.item.models import ItemType, ItemTypeProperty, Item, ItemProperty, ItemDrop, DropTable


class ItemTypeModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "classification")
    search_fields = ("id", "name", "classification")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class ItemTypePropertyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "item_type", "modifier_type", "stat_modified", "amount")
    search_fields = ("id", "item_type", "modifier_type", "stat_modified", "amount")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class ItemModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "classification")
    search_fields = ("id", "name", "classification")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class ItemPropertyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "item", "modifier_type", "stat_modified", "amount")
    search_fields = ("id", "item", "modifier_type", "stat_modified", "amount")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class DropTableModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "max_rate")
    search_fields = ("id", "name", "max_rate")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


class ItemDropModelAdmin(admin.ModelAdmin):
    list_display = ("id", "drop_table", "item_type", "drop_rate")
    search_fields = ("id", "drop_table", "item_type", "drop_rate")
    raw_id_fields = ("created_by", "updated_by",)
    list_per_page = 25


admin.site.register(ItemType, ItemTypeModelAdmin)
admin.site.register(ItemTypeProperty, ItemTypePropertyModelAdmin)
admin.site.register(Item, ItemModelAdmin)
admin.site.register(ItemProperty, ItemPropertyModelAdmin)
admin.site.register(DropTable, DropTableModelAdmin)
admin.site.register(ItemDrop, ItemDropModelAdmin)
