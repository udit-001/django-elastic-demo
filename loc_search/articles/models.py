from django.db import models

from taggit.managers import TaggableManager
from django.utils.text import slugify

from .utils import expert_article_upload_path
from tags.models import Tagged


class ExpertArticle(models.Model):
    DRAFT = "D"
    PUBLISHED = "P"
    STATUS = (
        (DRAFT, ("Draft")),
        (PUBLISHED, ("Published")),
    )
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(
        upload_to=expert_article_upload_path, blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    board = models.ForeignKey("categories.Board", on_delete=models.CASCADE, related_name="expert_articles")
    sub_category = models.ForeignKey("categories.SubCategory", on_delete=models.CASCADE, related_name="expert_articles")
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="expert_articles")
    description = models.TextField(max_length=20000)
    likes = models.ManyToManyField("auth.User", db_index=True, related_name="user_liked_expert_articles", blank=True)
    views = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=15, choices=STATUS,
                              default=DRAFT, null=True, blank=True, db_index=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(through=Tagged)
    # objects = ExpertArticleQuerySet.as_manager()

    class Meta:
        verbose_name = "Expert Article"
        verbose_name_plural = "Expert Articles"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ExpertArticleComment(models.Model):
    article = models.ForeignKey("articles.ExpertArticle", 
                on_delete=models.SET_NULL, blank=True, null=True, related_name="article_comments")
    comment = models.TextField(max_length=10000)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="expert_comments")

    parent_comment = models.ForeignKey("self", on_delete=models.SET_NULL, 
                blank=True, null=True, related_name="user_expert_article_comment_childrens")
    likes = models.ManyToManyField("auth.User", db_index=True, related_name="user_liked_expert_article_comments")

    # objects = ExpertArticleCommentQuerySet.as_manager()

    class Meta:
        verbose_name = "Expert Article Comment"
        verbose_name_plural = "Expert Article Comments"

    def __str__(self):
        return self.comment[:50]
