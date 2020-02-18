from django.db import models
from django.utils.text import slugify
from .util import board_thumbnail_upload_path, sub_category_thumbnail_upload_path


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    min_age = models.IntegerField(default=0)
    max_age = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    thumbnail = models.ImageField(
        upload_to=board_thumbnail_upload_path, blank=True, null=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)
    description = models.CharField(max_length=100)
    thumbnail = models.ImageField(
        upload_to=sub_category_thumbnail_upload_path, blank=True, null=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ExpertUserVideoCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Expert User Video Category"
        verbose_name_plural = "Expert User Video Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
