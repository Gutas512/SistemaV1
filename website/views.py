import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from Sistema.models import TBLusuarios
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.db import models
from django import forms

# Create your views here.

def lista_usuarios(request):

    usuarios = TBLusuarios.objetos.all()

    contexto = {'usuarios' : usuarios}

    return render(request, "templates/usuarios.html", contexto)

class ListaUsuarios(ListView):
    template_name = "templates/usuarios.html"
    model = TBLusuarios
    context_object_name = "usuarios"


class IndexTemplateView(TemplateView):
    template_name = "index.html"


class FormularioDeCriacao:
    pass


def criar_usuario(request, pk):
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ListaUsuarios'))


    else:
        return render(request,"templates/forms.html",{'form' : form})

class UsuarioListView(ListView):
    template_name = "website/lista.html"
    model = TBLusuarios
    context_object_name = "usuarios"

class UsuarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = TBLusuarios
    fields = '__all__'
    context_object_name = 'usuario'

    def get_object(self, queryset=None):

        id=self.kwargs.get(self.pk_url_kwarg)

        if id is not None:
            usuario = TBLusuarios.objetos.filter(id=id).first()

        return usuario

class UsuarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = TBLusuarios
    context_object_name = 'usuario'
    success_url = reverse_lazy(
        "website:lista_usuarios"
    )

class UsuarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = TBLusuarios
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_usuarios")

class InsereFuncionarioForm(forms.ModelForm):
    class meta:
        model = TBLusuarios
        fields = '__all__'
