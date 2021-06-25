from django.urls import path
from .views import BookCreateView,BookList,BookUpdate,BookDetailView,BookDeleteView,DBookCreate,DBookList,DBookUpdate,DBookDetail,DBookDelete
urlpatterns=[
  path("create",BookCreateView.as_view(),name="create"),
  path("list",BookList.as_view(),name="list"),
  path("books/<int:id>",BookUpdate.as_view(),name="update"),
  path("details/<int:id>",BookDetailView.as_view(),name="view"),
  path("remove/<int:id>",BookDeleteView.as_view(),name="remove"),
  path("dcreate",DBookCreate.as_view(),name="dcreate"),
  path("books/dlist",DBookList.as_view(),name="dlist"),
  path("books/<int:pk>",DBookUpdate.as_view(),name="dupdate"),
  path("detail/<int:pk>",DBookDetail.as_view(),name="detail"),
  path("delete/<int:pk>",DBookDelete.as_view(),name="delete")
]