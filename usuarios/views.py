from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Profile

def registro_view(request):
    # crea usuario y lo loguea
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido!')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    # valida y inicia sesion
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    # cierra sesion
    logout(request)
    messages.info(request, 'Has cerrado sesión.')
    return redirect('index')

def perfil_view(request):
    # actualiza foto perfil
    if not request.user.is_authenticated:
        return redirect('login')
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        if 'foto_perfil' in request.FILES:
            profile.foto_perfil = request.FILES['foto_perfil']
            profile.save()
            messages.success(request, 'Foto de perfil actualizada.')
        return redirect('perfil')
    return render(request, 'usuarios/perfil.html', {'profile': profile})
