from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView


class ListaProdutos(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Lista de produtos')


class DetalheProduto(DetailView):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe do produto')


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar ao carrinho')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover do carrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho de compras')


class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar compra')
