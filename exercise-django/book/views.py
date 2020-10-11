from django.shortcuts import render, redirect

# Create your views here.
from book.forms import BookForm, PublisherForm, AuthorForm
from book.models import Publisher, Author, Book


def pub_read(request):
    publishers = Publisher.objects.all()
    return render(request, 'book/all_publisher.html', {'publishers': publishers})


def pub_add(request):
    form = PublisherForm()
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher-all')
    return render(request, 'book/add_publisher.html', {'form': form})


def pub_del(request, id):
    publisher = Publisher.objects.get(pk=id)
    publisher.delete()
    return redirect('publisher-all')


def pub_edit(request, id):
    publisher = Publisher.objects.get(pk=id)
    form = PublisherForm(instance=publisher)
    if request.method == "POST":
        publisher.name = request.POST['name']
        publisher.save()
        return redirect('publisher-all')
    return render(request, 'book/edit_publisher.html', {'form': form, 'publisher': publisher})


def author(request):
    authors = Author.objects.all()
    return render(request, 'book/all_author.html', {'authors': authors})


def author_edit(request, id):
    auth = Author.objects.get(pk=id)
    form = AuthorForm(instance=auth)
    if request.method == "POST":
        auth.name = request.POST['name']
        auth.save()
        return redirect('author-all')
    return render(request, 'book/edit_author.html', {'form': form, 'auth': auth})


def all_books(request):
    books = Book.objects.all()
    return render(request, 'book/all_books.html', {'books': books})


def add_book(request):
    publishers = Publisher.objects.all()
    authors = Author.objects.all()
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        f = form.save(commit=False)
        pub = Publisher.objects.get(id=request.POST['publisher'])
        aut = Author.objects.get(id=request.POST['author'])
        f.publisher = pub
        f.save()
        this_book_id = Book.objects.latest('id')
        book = Book.objects.get(id=this_book_id.id)
        book.author.add(aut)
        return redirect('book-all')
    return render(request, 'book/add_book.html', {'form': form, 'publishers': publishers, 'authors': authors})

# def publisherCreate(request):
#     form = PublisherForm()
#     if request.method == 'POST':
#         form = PublisherForm(request.POST)
#         if form.is_valid():
#             form.save()
#     return render(request, 'book/add_publisher.html', {'form': form})
