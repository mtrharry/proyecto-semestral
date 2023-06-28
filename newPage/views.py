from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, logout, authenticate, login as auth_login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import SubscriptionForm
from .models import Usuario, tipoUsuario, Subscription

def blog(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/blog.html", context)

def catalogo(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/catalogo.html", context)

def contacto(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/contacto.html", context)

def login_registro(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/login_registro.html", context)

def nosotros(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/nosotros.html", context)

def registro(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/registro.html", context)

def suscripciones(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/suscripciones.html", context)

def perfil(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/perfil.html", context)

def index(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/index.html", context)

def crud(request):
    usuario = Usuario.objects.all()
    context = {"usuario": usuario}
    return render(request, "pages/user_list.html", context)


class UserAddForm(forms.Form):
    rut = forms.CharField(max_length=10)
    nombre = forms.CharField(max_length=50)
    appPaterno = forms.CharField(max_length=30)
    appMaterno = forms.CharField(max_length=30)
    fecha = forms.DateField()
    correo = forms.EmailField()
    telefono = forms.CharField(max_length=10)

def userAdd(request):
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data["rut"]
            nombre = form.cleaned_data["nombre"]
            appPaterno = form.cleaned_data["appPaterno"]
            appMaterno = form.cleaned_data["appMaterno"]
            fecha = form.cleaned_data["fecha"]
            correo = form.cleaned_data["correo"]
            telefono = form.cleaned_data["telefono"]
            password = request.POST["password"]
            direccion = request.POST["direccion"]

            # Check if rut, nombre, and correo already exist in the database
            if Usuario.objects.filter(rut=rut).exists():
                form.add_error("rut", "El rut ya está registrado.")
            if Usuario.objects.filter(nombre=nombre).exists():
                form.add_error("nombre", "El nombre ya está registrado.")
            if Usuario.objects.filter(correo=correo).exists():
                form.add_error("correo", "El correo ya está registrado.")

            if not form.errors:
                tipo_cliente, created = tipoUsuario.objects.get_or_create(tipoUsuario="cliente")

                # Create the user using create_user method and set the hashed password
                objUsuario = Usuario.objects.create_user(
                    rut=rut,
                    nombre=nombre,
                    appPaterno=appPaterno,
                    appMaterno=appMaterno,
                    fechaNacimiento=fecha,
                    tipoUsuario=tipo_cliente,
                    correo=correo,
                    telefono=telefono,
                    activo=1,
                    direccion=direccion,
                )
                objUsuario.set_password(password)
                objUsuario.save()

                context = {"mensaje": "Registrado Correctamente"}
                return render(request, "pages/registro.html", context)
        else:
            print("Form errors:", form.errors)
    else:
        form = UserAddForm()

    tipo = tipoUsuario.objects.all()
    context = {"form": form, "tipo": tipo}
    return render(request, "pages/registro.html", context)




def userDel(request, pk):
    context = {}
    try:
        user = Usuario.objects.get(rut=pk)

        user.delete()
        usuarios = Usuario.objects.all()
        context = {"mensaje": "OK Registro eliminado", "usuario": usuarios}
        return render(request, "pages/user_list.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {"mensaje": "Error, Rut no encontrado...", "usuario": usuarios}
        return render(request, "pages/user_list.html", context)


def userEdit(request, pk):
    if pk != "":
        user = Usuario.objects.get(rut=pk)
        tipo = tipoUsuario.objects.all()
        context = {"usuario": user, "tipo": tipo}
        return render(request, "pages/user_edit.html", context)
    else:
        context = {"mensaje": "Error, usuario no encontrado"}
        return render(request, "pages/user_list", context)


def userUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)

        user = Usuario()
        user.rut = rut
        user.nombre = nombre
        user.appPaterno = appPaterno
        user.appMaterno = appMaterno
        user.fechaNacimiento = fecha
        user.tipoUsuario = objTipo
        user.correo = correo
        user.telefono = telefono
        user.password = password
        user.direccion = direccion
        user.activo = 1
        user.save()

        tipo = tipoUsuario.objects.all()
        context = {"mensaje": "OK Registro modificado", "tipo": tipo, "usuario": user}

        return render(request, "pages/user_edit.html", context)
    else:
        usuarios = Usuario.objects.all()
        context = {"usuario": usuarios}
        return render(request, "pages/user_list.html", context)



def login_view(request):
    if request.method == 'POST':
        rut = request.POST['rut']
        password = request.POST['password']
        print("rut: ",rut," contraseña: ",password)
        user = authenticate(request, username=rut, password=password)  
        print(user)
        if user is not None:
            auth_login(request, user)
            messages.success(request, ('Login successful!'))
            return render(request, 'pages/index.html')
        else:
            error_message = "Invalid username or password."
            return render(request, 'pages/login_registro.html', {'error_message': error_message})
    else:
        return render(request, 'pages/login_registro.html')


def logout_view(request):
    logout(request)
    messages.success(request, ('logout successful!'))
    return redirect('index')


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = SubscriptionForm()

    return render(request, 'subscribe.html', {'form': form})

