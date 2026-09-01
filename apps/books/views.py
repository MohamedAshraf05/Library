# from django.utils import timezone
# from django.shortcuts import get_object_or_404, redirect, render
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.db import transaction
# from apps.books.models import Book
# from .models import Loan


# @login_required
# def borrow_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)

#     # منع استعارة نفس الكتاب مرتين في نفس الوقت
#     already_borrowed = Loan.objects.filter(
#         member=request.user, book=book, status='borrowed'
#     ).exists()

#     if already_borrowed:
#         messages.error(request, "You already have this book borrowed.")
#         return redirect('catalog:book_list')

#     with transaction.atomic():
#         # نعيد قراءة الكتاب جوه الـ transaction عشان الـ check يكون دقيق
#         book = Book.objects.select_for_update().get(id=book_id)

#         if book.available_copies < 1:
#             messages.error(request, "No copies available.")
#             return redirect('catalog:book_list')

#         book.available_copies -= 1
#         book.save()

#         Loan.objects.create(member=request.user, book=book, status='borrowed')

#     messages.success(request, "Book borrowed successfully.")
#     return redirect('loans:my_loans')


# @login_required
# def return_book(request, loan_id):
#     loan = get_object_or_404(Loan, id=loan_id, member=request.user, status='borrowed')

#     with transaction.atomic():
#         loan.status = 'returned'
#         loan.return_date = timezone.now()
#         loan.save()

#         book = Book.objects.select_for_update().get(id=loan.book_id)
#         book.available_copies += 1
#         book.save()

#     messages.success(request, "Book returned successfully.")
#     return redirect('loans:my_loans')


# @login_required
# def my_loans(request):
#     loans = Loan.objects.filter(member=request.user, status='borrowed').select_related('book')
#     return render(request, 'loans/my_loans.html', {'loans': loans})