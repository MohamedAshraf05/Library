from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.books.models import Loan


@login_required
def my_loans(request):
    loans = Loan.objects.filter(member=request.user, status='borrowed').select_related('book')
    return render(request, 'pages/my_loans.html', {'loans': loans})