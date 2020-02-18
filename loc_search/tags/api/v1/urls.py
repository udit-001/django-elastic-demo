from django.urls import path

from . import views


app_names = "tags"
urlpatterns = [
	path("", views.TagListAPIView.as_view(), name="tags_list_api_view"),
]