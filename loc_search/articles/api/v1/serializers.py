# from rest_framework import serializers

# from articles.models import ExpertArticle, ExpertArticleComment
# from categories.api.v1.serializers import BoardSerializer, SubCategorySerializer
# from experts.api.v1.serializers import ExperUserBasicProfileSerializer
# from parents.api.v1.serializers import ParentArticleProfileSerializer
# from tags.api.v1.serializers import TagListSerializerField, TaggitSerializer


# class ExpertArticleListSerializer(serializers.ModelSerializer):

#     board = BoardSerializer()
#     sub_category = SubCategorySerializer()
#     created_by = ExperUserBasicProfileSerializer()

#     class Meta:
#         model = ExpertArticle
#         fields = [
#             "id",
#             "title",
#             "thumbnail",
#             "slug",
#             "board",
#             "sub_category",
#             "created_by",
#             "views",
#             "timestamp",
#         ]

#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         if hasattr(instance, "likes_count"):
#             response["likes_count"] = instance.likes_count
#         if hasattr(instance, "comment_count"):
#             response["comment_count"] = instance.comment_count
#         return response


# class ExpertArticleSerializer(TaggitSerializer, ExpertArticleListSerializer):

#     tags = TagListSerializerField()

#     class Meta:
#         model = ExpertArticle
#         fields = [
#             "id",
#             "title",
#             "thumbnail",
#             "slug",
#             "board",
#             "description",
#             "sub_category",
#             "created_by",
#             "views",
#             "timestamp",
#             "tags",
#         ]

#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         if "request" in self.context and self.context["request"].user and self.context["request"].user.is_authenticated:
#             response["like_status"] = instance.like_status
#             if self.context["request"].user.is_parent:
#                 response["bookmark_status"] = instance.bookmark_status
#         return response


# class ExpertArticleCommentCreateSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ExpertArticleComment
#         fields = [
#             "id",
#             "comment",
#             "article",
#             "timestamp",
#             "parent",
#             "expert",
#             "anonymous_user",
#         ]
#         read_only_fields = ["id", "article", "timestamp", "parent", "expert"]

#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         if hasattr(instance, "parent"):
#             if instance.parent:
#                 response["parent"] = ParentArticleProfileSerializer(instance.parent).data
#         if hasattr(instance, "expert"):
#             if instance.expert:
#                 response["expert"] = ExperUserBasicProfileSerializer(instance.expert).data
#         return response


# class ExpertArticleCommentSerializer(serializers.ModelSerializer):

#     parent = ParentArticleProfileSerializer()
#     expert = ExperUserBasicProfileSerializer()

#     class Meta:
#         model = ExpertArticleComment
#         fields = [
#             "id",
#             "comment",
#             "article",
#             "timestamp",
#             "parent",
#             "expert",
#             "anonymous_user",
#         ]

#     def to_representation(self, instance):
#         response = super().to_representation(instance)
#         if hasattr(instance, "likes_count"):
#             response["likes_count"] = instance.likes_count
#         if hasattr(instance, "children_comment_count"):
#             response["children_comment_count"] = instance.children_comment_count
#         if "request" in self.context and self.context["request"].user and self.context["request"].user.is_authenticated:
#             response["like_status"] = instance.like_status
#         return response
        

# class ExpertArticleThreadCommentCreateSerializer(ExpertArticleCommentCreateSerializer):

#     class Meta:
#         model = ExpertArticleComment
#         fields = [
#             "id",
#             "comment",
#             "article",
#             "parent_comment",
#             "timestamp",
#             "parent",
#             "expert",
#             "anonymous_user",
#         ]
#         read_only_fields = ["id", "article", "timestamp", "parent", "expert", "parent_comment"]


# class ExpertArticleNotificationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ExpertArticle
#         fields = [
#             "id",
#             "title",
#             "thumbnail",
#             "slug",
#         ]


# class ExpertArticleCommentNotificationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ExpertArticleComment
#         fields = [
#             "id",
#             "comment",
#             "article",
#             "timestamp",
#         ]
