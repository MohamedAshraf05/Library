from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from apps.books.models import Book
from apps.books.models import Loan

@login_required
def return_book(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id, member=request.user, status='borrowed')

    with transaction.atomic():
        loan.status = 'returned'
        loan.return_date = timezone.now()
        loan.save()

        book = Book.objects.select_for_update().get(id=loan.book_id)
        book.available_copies += 1
        book.save()

    messages.success(request, "Book returned successfully.")
    return redirect('loans:my_loans')