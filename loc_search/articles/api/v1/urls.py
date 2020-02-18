# from django.urls import path

# from . import views

# app_name = "articles"
# urlpatterns = [
#     path("expert-articles/", views.ExpertArticleView.as_view(), name="expert_articles"),
#     path("all-articles/", views.AllArticleAPIView.as_view(), name="all_articles"),
#     path("comments/", views.ExpertArticleCommentView.as_view(), name="expert_articles_comments"),

#     path("<int:article_id>/comments/create/",
#             views.ExpertArticleCommentCreateView.as_view(),
#             name="expert_articles_comments_create"),

#     path("comments/<int:comment_id>/like/",
#             views.ExpertArticleCommentLikeApiView.as_view(),
#             name="expert_article_comments_like_api_view"),

#     path("comments/<int:comment_id>/thread/",
#             views.ExpertArticleThreadCommentView.as_view(),
#             name="expert_article_comments_thread_api_view"),

    
#     path("<int:article_id>/comments/<int:comment_id>/thread/create/",
#             views.ExpertArticleThreadCommentCreateView.as_view(),
#             name="article_comments_thread_create_api_view"),
    
#     path("<int:article_id>/like/",
#             views.ExpertArticleLikeApiView.as_view(),
#             name="article_like_api_view"),

#     path("<slug:slug>/related-articles/",
#             views.RelatedExpertArticleListView.as_view(),
#             name="related_expert_articles_list"),

#     path("<slug:slug>/",
#             views.ExpertArticleDetailView.as_view(),
#             name="expert_articles_detail"),
# ]