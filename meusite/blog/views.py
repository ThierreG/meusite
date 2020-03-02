from django.shortcuts import render


def entrar(request):
    return render(request,'entrar.html')

def sair(request):
    return render(request,'sair.html')

def cadastrar(request):
    return render(request,'cadastrar.html')