from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic
# from django.contrib.auth.models import User

from .models import CustomUser
from django.contrib import messages


from .forms import CustomUserCreationForm


def user_list(request):
    return render(request, 'user_list.html')

def register_login (request):
    if request.method == 'POST':
        email = request.POST['email']
        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'This email address is already registered.')
            return redirect('landing')
        else:
            # Create a new user with the email as username
            user = CustomUser.objects.create_user(username=email, email=email)
            user.save()
            messages.success(request, 'Thank you for registering. Please check your email for further instructions.')
            return redirect('landing')
    else:
        # Render the landing page template
        return render(request, 'register.html')