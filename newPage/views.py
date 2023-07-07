from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model, logout, authenticate, login as auth_login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django import forms
from .models import Usuario, tipoUsuario, Subscription, Producto, Plan
from .Carrito import Carrito

def blog(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/blog.html", context)

def catalogo(request):
    productos = Producto.objects.all()
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/catalogo.html", {'productos':productos})

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
    user_subscription = Subscription.objects.get(user=request.user)
    context = {"subscription": user_subscription}
    return render(request, "pages/suscripciones.html", context)

def perfil(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/perfil.html", context)

def index(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/index.html", context)


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

staff_member_required(login_url='login')
def userDel(request, pk):
    try:
        user = Usuario.objects.get(rut=pk)
        is_superuser = user.is_superuser 
        user.delete()
        if is_superuser:
            messages.success(request, 'Registro eliminado correctamente (Superuser)')
            return redirect('crud') 
        else:
            messages.success(request, 'Registro eliminado correctamente (User)')
            return redirect('index') 
    except Usuario.DoesNotExist:
        messages.error(request, 'Error: Rut no encontrado')
    
    return redirect('user_list') 


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


def unsubscribe(request):
    subscription = Subscription.objects.get(user=request.user)
    subscription.delete()
    return redirect('suscripciones')


def subscribe(request):
    user = request.user

    try:
        subscription = Subscription.objects.get(user=user)
        if request.method == 'POST':
            plan_id = request.POST.get('plan')
            plan = get_object_or_404(Plan, pk=plan_id)
            subscription.plan = plan
            subscription.start_date = timezone.now().date()
            subscription.end_date = subscription.start_date + timezone.timedelta(days=30) 
            subscription.save()

            return redirect('suscripciones') 

        plans = Plan.objects.all()
        context = {'subscription': subscription, 'plans': plans}
        return render(request, 'pages/suscripciones.html', context)

    except Subscription.DoesNotExist:
        if request.method == 'POST':
            plan_id = request.POST.get('plan')
            plan = get_object_or_404(Plan, pk=plan_id)
            start_date = timezone.now().date()
            end_date = start_date + timezone.timedelta(days=30)  

            subscription = Subscription(user=user, plan=plan, start_date=start_date, end_date=end_date)
            subscription.save()

            return redirect('suscripciones') 

        plans = Plan.objects.all()
        return render(request, 'pages/suscripciones.html', {'plans': plans})


def crud(request):
    usuario = Usuario.objects.all()
    plans = Plan.objects.all()

    if request.method == 'POST' and 'delete_plan' in request.POST:
        plan_id = request.POST.get('delete_plan')
        plan = Plan.objects.get(pk=plan_id)
        plan.delete()
        return redirect('crud')

    elif request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        plan = Plan(name=name, price=price)
        plan.save()
        return redirect('crud')

    context = {"usuario": usuario, "plans": plans}
    return render(request, "pages/user_list.html", context)



def my_view(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    context = {'subscriptions': subscriptions}
    return render(request, 'perfil.html', context)


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("catalogo")


def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("catalogo")


def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("catalogo")


def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("catalogo")