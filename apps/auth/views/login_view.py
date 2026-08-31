from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        login_input = request.POST.get('username')
        pass_word = request.POST.get('password')
        
        username_to_auth = login_input

        # Check if the user entered an email instead of username
        user_by_email = User.objects.filter(email=login_input).first()
        if user_by_email:
            username_to_auth = user_by_email.username

        # Try to log the user in
        user = authenticate(request, username=username_to_auth, password=pass_word)

        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'auth/login.html', {'error': 'Username/Email or password is invalid'})

    return render(request, 'auth/login.html')
