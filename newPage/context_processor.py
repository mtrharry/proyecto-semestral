from .models import Subscription


def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    else:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
        
    if request.user.is_authenticated and Subscription.objects.filter(user=request.user).exists():
        total -= total * 0.05  
    return {"total_carrito": total}
