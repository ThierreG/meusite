from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class cadastrousuarioform(UserCreationForm):
    primeiro_nome = forms.CharField(label='primeiro_nome', max_length=50, required=True ,help_text='campo de nome obrigatorio ')
    ultimo_nome =  forms.CharField(label='ultimo_nome', max_length=50, required=True ,help_text='campo de nome obrigatorio ')
    email = forms.EmailField(label='E-mail', max_length= 250, help_text='por favor informe ' )


    class meta:
        model = User
        fields = [
            'username',
            'primeiro_nome',
            'ultimo_nome',
            'email',
            'password1',
            'password2',

        ]

