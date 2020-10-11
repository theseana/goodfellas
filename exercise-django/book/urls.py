from django.urls import path

from book import views

urlpatterns = [
    path('',  views.all_books, name='book-all'),
    path('all/authors', views.author, name="author-all"),
    path('all/publisher', views.pub_read, name="publisher-all"),

    path('add/book', views.add_book, name='book-add'),
    path('add/publisher', views.pub_add, name="publisher-add"),

    path('edit/author&id=<int:id>', views.author_edit, name="author-edit"),
    path('edit/publisher&id=<int:id>', views.pub_edit, name="publisher-edit"),

    path('delete/publisher&id=<int:id>', views.pub_del, name="publisher-delete"),
    ]
