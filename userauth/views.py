# userauth/views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm, IPOForm
from .models import User, IPO
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
import random
import string
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials!')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html', {'name': request.user.name})


@login_required
def manage_ipo_view(request):
    ipos_list = IPO.objects.all().order_by('-id')  # Order by latest
    paginator = Paginator(ipos_list, 10)  # Show 10 IPOs per page

    page_number = request.GET.get('page')
    ipos = paginator.get_page(page_number)
    return render(request, 'manage_ipo.html', {'name': request.user.name, 'ipos': ipos})


def is_superuser(user):
    return user.is_superuser


@login_required
@user_passes_test(is_superuser)
def register_ipo_view(request):
    if request.method == 'POST':
        form = IPOForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'IPO registered successfully!')
            return redirect('manage_ipo')
    else:
        form = IPOForm()
    return render(request, 'register_ipo.html', {'form': form})
@login_required
@user_passes_test(is_superuser)
def edit_ipo_view(request, ipo_id):
    ipo = get_object_or_404(IPO, id=ipo_id)
    if request.method == 'POST':
        form = IPOForm(request.POST, request.FILES, instance=ipo)
        if form.is_valid():
            form.save()
            messages.success(request, 'IPO updated successfully!')
            return redirect('manage_ipo')
    else:
        form = IPOForm(instance=ipo)
    return render(request, 'edit_ipo.html', {'form': form, 'ipo': ipo})


@login_required
@user_passes_test(is_superuser)
def delete_ipo_view(request, ipo_id):
    ipo = get_object_or_404(IPO, id=ipo_id)
    if request.method == 'POST':
        ipo.delete()
        messages.success(request, 'IPO deleted successfully!')
        return redirect('manage_ipo')
    return render(request, 'delete_ipo.html', {'ipo': ipo})
def user_side(request):
    ipos = IPO.objects.all()  # Fetch all IPO records from the database
    return render(request, 'userside.html', {'ipos': ipos})
def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

def forgot_password_view(request):
    return render(request, 'forgot.html')