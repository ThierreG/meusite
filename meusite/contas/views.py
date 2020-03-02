from django.shortcuts import render,redirect
from .forms import CadastroUsuarioForm

# Create your views here.


def entrar(request):
    return render(request,'entrar.html')

def sair(request):
    return render(request,'sair.html')

def cadastrar(request):
    
    #form = UserCreationForm()
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('entrar')
    else :
        form = CadastroUsuarioForm (request.POST)
        form = UserCreationForm()


    return render(
        request,'cadastrar.html',
        {'form': form}
        )

