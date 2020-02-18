from django.db import models

from taggit.models import TagBase, GenericTaggedItemBase


class CustomTag(TagBase):
    similar_tag = models.ManyToManyField("self", blank=True)


class Tagged(GenericTaggedItemBase):
    tag = models.ForeignKey(
        CustomTag,
        related_name="%(app_label)s_%(class)s_items",
        on_delete=models.SET_NULL,
        null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
