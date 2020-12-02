"""GestionFactureTelephonique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include

from factureTelephonique.views import *

urlpatterns = [
                  url(r'admin/', admin.site.urls),
                  url('factureTelephonique', include('factureTelephonique.urls'), name="factureTelephonique"),

                  url('menu',view= menu,name="menu"),
                  url('logout',view= logoutPage,name="logout"),
                  url('about',view= aboutPage,name="about"),
                  url('gestionClient',view= getAllClient,name="Clients"),
                  url(r'delete/(?P<id>.+)',view= deleteClient,name="deleteClient"),
                  url('addC',view= addClient,name="addClient"),
                  url('cdr',view= getAllCdr,name="gestionCdr"),
                  url('ajouterCdr',view= addCdr,name="addCdr"),
                  url(r'delete/(?P<id>.+)',view= deleteCdr,name="deleteCdr"),
                  url('addFacture',view= addFacture,name="addFacture"),
                  url('factures',view= getAllFacture,name="gestionFacture"),
                  url('searchCdr',view= searchCdr,name="searchCdr"),
                  url('lireFacture/(?P<id>.+)',view= lireFacture,name="lireFacture"),
                  url(r'edit/(?P<id>.+)',view= editFacture,name="editFacture"),
                  url(r'^$', view=loginPage, name="login")  # ^$ qui commence et se termine par rien)
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'factureTelephonique.views.error_404_view'
