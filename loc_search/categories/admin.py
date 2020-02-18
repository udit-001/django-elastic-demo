from django.contrib import admin

from .models import Board, SubCategory, ExpertUserVideoCategory


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "min_age",
        "max_age",
        "description",
        "slug",
        "thumbnail",
        "active",
    )
    list_filter = ("active",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ["name"]}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "description",
        "thumbnail",
        "active",
    )
    list_filter = ("active",)
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ["name"]}


@admin.register(ExpertUserVideoCategory)
class ExpertUserVideoCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ["name"]}
