from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import ExpertArticle
from tags.models import CustomTag


@registry.register_document
class ExpertArticleDocument(Document):

    tags = fields.ObjectField(properties={
        'name': fields.TextField(),
        'slug': fields.TextField(),
    })

    id = IntegerField(attr="id")
    
    class Index:
        name = 'articles'

    class Django:
        model = ExpertArticle
        fields = [
            "title",
            "slug",
            "description",
            "views",
            "timestamp",
        ]
        related_models = [CustomTag]
