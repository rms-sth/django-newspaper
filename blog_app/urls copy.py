from django.urls import path
from blog_app import views

urlpatterns = [
    path(
        "",
        views.post_list,
        name="post-list",
    ),
    path(
        "post-detail/<int:pk>/",
        views.post_detail,
        name="post-detail",
    ),
    path(
        "draft-list/",
        views.draft_list,
        name="draft-list",
    ),
    path(
        "post-create/",
        views.post_create,
        name="post-create",
    ),
    path(
        "post-publish/<int:pk>/",
        views.post_publish,
        name="post-publish",
    ),
    path(
        "post-delete/<int:pk>/",
        views.post_delete,
        name="post-delete",
    ),
    path(
        "post-update/<int:pk>/",
        views.post_update,
        name="post-update",
    ),
]
