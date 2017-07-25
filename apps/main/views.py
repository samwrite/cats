from django.shortcuts import render, redirect
from .models import Cat, User
from django.contrib import messages
from django.core.urlresolvers import reverse
def index(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    context = {
        "user": User.objects.get(id = request.session['id']).first_name,
        "cats": Cat.objects.all().order_by("-likes")
    }
    return render(request,"main/index.html", context)
def logout(request):
    request.session.pop('id')
    return redirect(reverse("loginreg:index"))
def addCatPage(request):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    return render(request, "main/addCat.html")
def addCat(request):
    result = Cat.objects.addCat(request.POST, request.session)
    if result['status'] == False:
        for error in result['error']:
            messages.error(request, error)
        return redirect(reverse("main:addCatPage"))
    return redirect(reverse("main:index"))
def addLike(request, cat_id):
    Cat.objects.addLike(cat_id)
    return redirect(reverse("main:index"))
def catInfo(request, cat_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    context = { "cats" : Cat.objects.filter(id = cat_id) }
    return render(request,"main/catInfo.html",context)
def Delete(request, cat_id):
    Cat.objects.get(id = cat_id).delete()
    return redirect(reverse("main:index"))
def updatePage(request, cat_id):
    if 'id' not in request.session:
        return redirect(reverse('loginreg:index'))
    context = { "cats" : Cat.objects.filter(id = cat_id) }
    return render(request, "main/Update.html", context)
def updateInfo(request, cat_id):
    Cat.objects.UpdateInfo(request.POST, cat_id)
    return redirect(reverse("main:index"))