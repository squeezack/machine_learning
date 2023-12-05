from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import FormLogin
from django.contrib.auth import logout

def login_view(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect ke halaman setelah login berhasil
                return redirect('dashboard')  # Ganti dengan nama URL halaman setelah login
            else:
                # Tambahkan pesan kesalahan jika login tidak berhasil
                form.add_error(None, 'Login failed. Please check your username and password.')
    else:
        form = FormLogin()

    return render(request, 'pages/login/index.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
