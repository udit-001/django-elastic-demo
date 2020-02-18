from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import CustomTag


@registry.register_document
class CustomTagDocument(Document):

    class Index:
        name = "tags"

    class Django:
        model = CustomTag
        fields = [
            "name",
            "slug",
        ]

