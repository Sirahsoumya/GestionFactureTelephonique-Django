from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from factureTelephonique.forms import clientForms, CdrFroms, FactureFroms
from factureTelephonique.models import *


def loginPage(request):
    if request.user.is_authenticated:
        return render(request, "menu.html")
    if request.method=='POST':
        password=request.POST.get('password')
        log=request.POST.get('username')
        user=authenticate(request,username=log , password=password)
        if user is not None and user.is_superuser:
            login(request,user)
            return redirect('/menu')
        else:
            messages.error(request,"username or password is incorrect")

    return render(request, 'login.html')


def menu(request):
    if request.user.is_authenticated:
        return render(request, "menu.html")
    return redirect('/')


def logoutPage(request):
    logout(request)
    return redirect('login')


def aboutPage(request):
    return render(request, "About.html")


def addClient(request):
    form = clientForms()
    if request.method == 'POST':
        form = clientForms(request.POST)
        if form.is_valid():
            form.save()

            return redirect('Clients')
        # messages.success(request, 'le client a ete bien ajoute')

    return render(request, "addClient.html", {'form': form})


def getAllClient(request):
    clients = Client.objects.all()
    return render(request, "listeClient.html", {'clients': clients})





def getAllCdr(request):
    cdrs = Cdr.objects.all()
    if request.method== 'POST':
        search_cdr=request.POST.get('findCdr')
        cdrs=Cdr.objects.filter(date=search_cdr)
    return render(request, "listeCdr.html", {'cdrs': cdrs})


def addCdr(request):
    formc = CdrFroms()
    print(request.method)
    if request.method == 'POST':
        formc = CdrFroms(request.POST)

        if formc.is_valid():
            instance=formc.save()
            print ("test",instance)
            return redirect('gestionCdr')

    return render(request, "addCdr.html", {'formc': formc})


def deleteCdr(request, id):
    cdr = Cdr.objects.get(id=id)
    cdr.delete()
    return redirect('gestionCdr')


def deleteClient(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect('Clients')


def addFacture(request):
    formF = FactureFroms()
    if request.method == 'POST':
        formF = FactureFroms(request.POST)
        if formF.is_valid():
            formF.save()
            return redirect('gestionFacture')

    return render(request, "addFacture.html", {'formF': formF})


def getAllFacture(request):
    factures = Facture.objects.all()
    return render(request, "listeFacture.html", {'factures': factures})


def editFacture(request, id):
    facture = Facture.objects.get(id=id)
    formF= FactureFroms(instance=facture)
    if request.method=='POST':
        formF=FactureFroms(request.POST,instance=facture)
        if formF.is_valid():
            print('entree ou pas!!')
            formF.save()
            return redirect('gestionFacture')
    return render(request, "EditFacture.html", locals())


def searchCdr(request):
  return render(request,"searchCdr.html")

def lireFacture(request,id):
    facture=Facture.objects.get(id = id)
    return render(request,"FichierFacture.html",locals())


def error_404_view(request,exception):

     return render('404.html')
