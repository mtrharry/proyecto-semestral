from .models import Usuario, tipoUsuario
from django.forms import ModelForm
from django import forms
from .models import Subscription

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"


class tipoForm(ModelForm):
    class Meta:
        model = tipoUsuario
        fields = [
            "tipoUsuario",
        ]
        labels = {
            "tipoUsuario": "tipoUsuario",
        }

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']