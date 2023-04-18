from django.urls import path

from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista_produtos'),
    path('<slug>', views.DetalheProduto.as_view(), name='detalhe_produto'),
    path('adicionaraocarrinho/', views.AdicionarAoCarrinho.as_view(),
         name='adicionar_ao_carrinho'),
    path('removerdocarrinho/', views.RemoverDoCarrinho.as_view(),
         name='remover_do_carrinho'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('finalizar/', views.Finalizar.as_view(), name='finalizar'),
]
