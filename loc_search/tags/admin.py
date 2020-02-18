from django.contrib import admin

from .models import CustomTag, Tagged


@admin.register(CustomTag)
class CustomTagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    # raw_id_fields = ("similar_tag",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Tagged)
class TaggedAdmin(admin.ModelAdmin):
    list_display = ("id", "content_type", "object_id", "tag", "timestamp")
    list_filter = ("content_type", "tag", "timestamp")
