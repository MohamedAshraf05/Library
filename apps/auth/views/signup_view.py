from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def signup_view(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')



        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'auth/signup.html', {
                'error': 'Username already exists. Please choose another one.'
            })

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'auth/signup.html', {
                'error': 'Email already exists. Please use another email.'
            })

        # Create new user
        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )

        return redirect('login')

    return render(request, 'auth/signup.html')