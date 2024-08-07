from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LivroForm, PreferenciasForm
from .models import Livro

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistroForm()
    return render(request, 'biblioteca/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'biblioteca/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def adicionar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.usuario = request.user
            livro.save()
            return redirect('dashboard')
    else:
        form = LivroForm()
    return render(request, 'biblioteca/adicionar_livro.html', {'form': form})

@login_required
def dashboard(request):
    livros = Livro.objects.filter(usuario=request.user)
    cor_fundo = request.session.get('cor_fundo', '#ffffff')
    return render(request, 'biblioteca/dashboard.html', {'livros': livros, 'cor_fundo': cor_fundo})

@login_required
def personalizar(request):
    if request.method == 'POST':
        form = PreferenciasForm(request.POST)
        if form.is_valid():
            cor_fundo = form.cleaned_data['cor_fundo']
            request.session['cor_fundo'] = cor_fundo
            return redirect('dashboard')
    else:
        form = PreferenciasForm()
    return render(request, 'biblioteca/personalizar.html', {'form': form})

