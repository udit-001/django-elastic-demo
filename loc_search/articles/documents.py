from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import ExpertArticle
from categories.models import Board, SubCategory
from tags.models import CustomTag


@registry.register_document
class ExpertArticleDocument(Document):

    tags = fields.ObjectField(properties={
        'name': fields.TextField(),
        'slug': fields.TextField(),
    })

    board = fields.ObjectField(properties={
        "name": fields.TextField(),
        "min_age": fields.IntegerField(),
        "max_age": fields.IntegerField(),
        "slug": fields.TextField()
    })

    sub_category = fields.ObjectField(properties={
        "name": fields.TextField(),
        "slug": fields.TextField()
    })

    id = fields.IntegerField()

    timestamp = fields.DateField()
    
    class Index:
        name = 'articles'

    class Django:
        model = ExpertArticle
        fields = [
            "title",
            "slug",
            "description",
            "views",
            # "timestamp"
        ]
        related_models = [CustomTag, Board, SubCategory]

        def get_queryset(self):
        """Not mandatory but to improve performance we can select related in one sql request"""
                return super().get_queryset().prefetch_related("tags").select_related(
                    "board", "sub_category"
                )
