from django.contrib import admin
from apps.books.models import Book , Loan

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'available_copies', "total_copies" , "category" , "id")
    search_fields = ('title', 'author', 'isbn')


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book__title', 'member', 'borrow_date', 'return_date', 'status')
    search_fields = ('book__title', 'member__username')