from django.shortcuts import render, redirect, get_object_or_404
from ..models import Book
from first_app.models import Book

def book_list(request):

    books = Book.objects.all() # retrive all books db
    context = {
        'books':books,
        'massage': 'This is FBVs'
    }
    return render(request, 'books/book_list.html',context)