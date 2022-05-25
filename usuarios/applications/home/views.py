import datetime
from multiprocessing import context

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin #siempre que se necesite algo de usuarios...
#se encuentra en django.contrib.auth...
from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView


#un Mixin sirve como herencia en POO pero en Django, cuando hay un codigo que debe...
#repetirse varias veces porque se debe utilizar esa funcionalidad en repetidas vistas...
#para evitar repetir codigo, se utiliza el mixin para extender esa funcionalidad...
# a las vistas que lo requieran
class FechaMixin(object):

    def get_context_data(self, **kwargs):
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.datetime.now
        return context


class HomePage(LoginRequiredMixin,TemplateView):
    template_name = "home/index.html"
    #El "LoginRequiredMixin" es un mixin que nos ayuda a que si un usuario no esta logueado...
    #e intente acceder a una ruta, en vez de motrarle la ruta, le redirija a otra ruta...
    #que deseemos hasta que se loguee y pueda navegar sin problemas

    #El mixin "LoginRequiredMixin" requiere del campo "login_url" que sirve para redirigir...
    #a otra parte cuando no esta logueado
    login_url = reverse_lazy('users_app:user-login')
    #con el reverse_lazy se maneja urls dentro de las clases

#para poder extender el mixin en una vista, se debe pasar como parametro y luego el tipo de...
#vista a utilizar en la vista basada en clase
#al tener el mixin ya tengo acceso y puedo heredar el context si la vista generica utiliza...
#el metodo get_context_data
class TemplatePruebaMixin(FechaMixin, TemplateView):
    template_name = "home/mixin.html"