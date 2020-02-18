from rest_framework import serializers
from accounts.api.v1.serializers import UserSerializer
from articles.models import ExpertArticle, ExpertArticleComment
from parents.models import ParentProfile
from experts.models import ExpertUserProfile
from discussions.models import Discussion, DiscussionComment
from videos.models import ExpertUserVideo, ExpertVideoComment
from articles.api.v1.serializers import ExpertArticleNotificationSerializer, ExpertArticleCommentNotificationSerializer
from discussions.api.v1.serializers import DiscussionNotificationSerializer, DiscussionCommentNotificationSerializer
from experts.api.v1.serializers import ExperUserBasicProfileSerializer
from parents.api.v1.serializers import ParentArticleProfileSerializer
from videos.api.v1.serializers import ExpertUserVideoNotificationSerializer, ExpertUserVideoCommentNotificationSerializer


class GenericNotificationRelatedField(serializers.RelatedField):

    def to_representation(self, instance):
        if isinstance(instance, ExpertArticle):
            serializer = ExpertArticleNotificationSerializer(instance)
        if isinstance(instance, ParentProfile):
            serializer = ParentArticleProfileSerializer(instance)
        if isinstance(instance, ExpertUserProfile):
            serializer = ExperUserBasicProfileSerializer(instance)
        if isinstance(instance, Discussion):
            serializer = DiscussionNotificationSerializer(instance)
        if isinstance(instance, ExpertUserVideo):
            serializer = ExpertUserVideoNotificationSerializer(instance)
        if isinstance(instance, ExpertArticleComment):
            serializer = ExpertArticleCommentNotificationSerializer(instance)
        if isinstance(instance, DiscussionComment):
            serializer = DiscussionCommentNotificationSerializer(instance)
        if isinstance(instance, ExpertVideoComment):
            serializer = ExpertUserVideoCommentNotificationSerializer(instance)
        return serializer.data
