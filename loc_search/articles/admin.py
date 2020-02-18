from django.contrib import admin

from .models import ExpertArticle, ExpertArticleComment
# from categories.models import Board, SubCategory


@admin.register(ExpertArticle)
class ExpertArticleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "thumbnail",
        "slug",
        "board",
        "sub_category",
        "created_by",
        "views",
        "status",
        "timestamp",
    )
    list_filter = ("board", "sub_category", "created_by", "timestamp")
    raw_id_fields = ("likes", "tags")
    search_fields = ("slug",)


@admin.register(ExpertArticleComment)
class ExpertArticleCommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "article",
        "timestamp",
        "parent_comment",
    )
    list_filter = (
            "timestamp",
        )
    raw_id_fields = ("likes",)
