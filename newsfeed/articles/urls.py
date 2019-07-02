from django.urls import include, path, re_path

from .views import (
    ArticleDetailView, 
    ArticleListView,
    CommentListView,
    CommentsView,
    SubjectListView
)


#TODO: The detail url has to be on top or else it will be
# overwritten by the list view. This may need to be corrected
# so order is not as important
app_name = "articles"
urlpatterns = [
    path(r'', ArticleListView.as_view(), name='articles'),
    re_path(r'(?P<slug>.+)/comments/$', CommentsView.as_view()),
    re_path(r'(?P<slug>.+)/$', ArticleDetailView.as_view()),
    re_path(r'(?P<subject>.+)/$', SubjectListView.as_view()),
]
