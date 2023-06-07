from django.shortcuts import render
from .models import Usuario, tipoUsuario

# Create your views here.

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

def index(request):
    usuario = Usuario.objects.all()
    context = {"user": usuario}
    return render(request, "pages/index.html", context)

def crud(request):
    usuario = Usuario.objects.all()
    context = {"usuario": usuario}
    return render(request, "pages/user_list.html", context)


def userAdd(request):
    if request.method != "POST":
        tipo = tipoUsuario.objects.all()
        context = {"tipo": tipo}
        return render(request, "pages/user_add.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)
        objUsuario = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            appPaterno=appPaterno,
            appMaterno=appMaterno,
            fechaNacimiento=fecha,
            tipoUsuario=objTipo,
            correo=correo,
            telefono=telefono,
            activo=1,
        )
        objUsuario.save()
        context = {"mensaje": "OK Registrado Correctamente"}
        return render(request, "pages/user_add.html", context)


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
        user.activo = 1
        user.save()

        tipo = tipoUsuario.objects.all()
        context = {"mensaje": "OK Registro modificado", "tipo": tipo, "usuario": user}

        return render(request, "pages/user_edit.html", context)
    else:
        usuarios = Usuario.objects.all()
        context = {"usuario": usuarios}
        return render(request, "pages/user_list.html", context)
