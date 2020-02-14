from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import City


@registry.register_document
class CityDocument(Document):
    class Index:
        name = 'city'

    geocoords = fields.GeoPointField()

    def prepare_geocoords(self, instance):
        return {
            'lon': instance.longitude,
            'lat': instance.latitude
        }

    class Django:
        model = City
        fields = [
            'country',
            'postal_code',
            'place_name',
            'admin_name1',
            'admin_code1',
            'admin_name2',
            'admin_code2',
            'admin_name3',
            'admin_code3',
            'latitude',
            'longitude',
            'accuracy'
        ]

