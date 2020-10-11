from django.contrib import admin

# Register your models here.
from book.models import Publisher, Author, Book

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
