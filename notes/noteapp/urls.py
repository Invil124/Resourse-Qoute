from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import AddTagView, AddAuthorView, AddQuoteView, QuoteView, AuthorView

app_name = "noteapp"

urlpatterns = [
    path("", views.main, name="main"),
    path("add_tag/", login_required(AddTagView.as_view()), name="add_tag"),
    path("add_author/", login_required(AddAuthorView.as_view()), name="add_author"),
    path("add_quote/", login_required(AddQuoteView.as_view()), name="add_quote"),
    path("quote/<int:quote_id>", QuoteView.as_view(), name="quote"),
    path("author/<str:full_name>", AuthorView.as_view(), name="author")
]