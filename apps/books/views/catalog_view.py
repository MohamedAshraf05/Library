from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from apps.books.models import Book

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

def catalog(request):
    books = Book.objects.all()
    return render(request, 'pages/catalog.html', {'books': books})

def book_detail_view(request, pk):
    """Display detailed information about a specific book"""
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'pages/book_detail.html', {
        'book': book
    })
