from django.conf.urls import include, url
from shelf.views import AuthorListView, AuthorDetailView, BookListView

urlpatterns = [
    url(r'^autorzy/$', AuthorListView.as_view(), name='author-list'),
    url(r'^autorzy/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^ksiazki/$', BookListView.as_view(), name='book-list'),
]