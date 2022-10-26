from django.urls import path
from . import views

# Retrieve the URL for your landing page
urlpatterns = [
    path(
        "",
       views.CardListView.as_view(),
        name="card-list"
    ),
    path(
        "new_card",
        views.CardCreateView.as_view(),
        name="card-create"
    ),
    path(
        "edit/<int:pk>",
        views.CardUpdateView.as_view(),
        name="card-update"
    ),
    path(
        "box/<int:box_num>",
        views.BoxView.as_view(),
        name="box",
    ),
    path(
        "new_group",
        views.NewGroupView.as_view(),
        name="new-group",
    )
]
