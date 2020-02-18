from django_filters import rest_framework as filters
from tags.models import CustomTag


class TagsFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CustomTag
        fields = ["name",]
