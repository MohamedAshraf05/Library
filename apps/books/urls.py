from django.urls import path
from apps.books.views import borrow_book , return_book , my_loans , catalog , book_detail_view

app_name = 'loans'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('book/<int:pk>/', book_detail_view, name='book_detail'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('return/<int:loan_id>/', return_book, name='return_book'),
    path('my-loans/', my_loans, name='my_loans'),
]