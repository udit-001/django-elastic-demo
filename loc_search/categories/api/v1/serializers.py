from rest_framework import serializers

from categories.models import Board, ExpertUserVideoCategory, SubCategory


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = [
            "id",
            "name",
            "min_age",
            "max_age",
            "slug",
            "thumbnail",
        ]


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = [
            "id",
            "name",
            "slug",
            "thumbnail",
        ]


class ExpertUserVideoCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpertUserVideoCategory
        fields = [
            "id",
            "name",
            "slug",
        ]

