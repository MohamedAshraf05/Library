from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def signup_view(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')

        # Save new user
        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=user_name,
            password=pass_word
        )

        return redirect('login')

    return render(request, 'auth/signup.html')