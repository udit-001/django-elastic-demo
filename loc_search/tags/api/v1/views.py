from django.db.models import Count

from rest_framework import generics

from .serializers import CustomTagSerializer
from tags.filters import TagsFilter
from tags.models import CustomTag


class TagListAPIView(generics.ListAPIView):
    serializer_class = CustomTagSerializer
    filterset_class = TagsFilter

    def get_queryset(self):
    	queryset = CustomTag.objects.all().annotate(
                    parent_following_count=Count("followers")
                ).order_by("-parent_following_count")
    	return queryset