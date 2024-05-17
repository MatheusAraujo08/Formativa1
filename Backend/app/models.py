from django.db import models



class CategoriaProdutos(models.Model):
    nome = models.CharField(max_length=150)

    def __strl__(self):
        return self.nome
    
 

class Produtos(models.Model):
    categoriaFK = models.ForeignKey(CategoriaProdutos, related_name='categoriaProdutos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade = models.IntegerField()
    

    def __strl__(self):
        return self.nome
    

class Foto(models.Model):
    url = models.CharField(max_length=15000)
    produtosFK = models.ForeignKey(Produtos, related_name='produtos', on_delete=models.CASCADE)

    def __strl__(self):
        return self.url
    

class Peca(models.Model):
    nome = models.CharField(max_length=150)
    medidas = models.CharField(max_length=150)
    peso = models.CharField(max_length=150)
    produtosFK = models.ForeignKey(Produtos, related_name='produtos', on_delete=models.CASCADE)

    def __strl__(self):
        return self.nome

STATUS_PAGAMENTOS = [
    ("P","PENDENTE"),
    ("A","APROVADO"),
    ("R","RECUSADO"),
    ("C","CANCELADO"),
]

class Vendas(models.Model):
    #usuarioFK = models.ForeignKey(UsuarioCustomizado, related_name='usuarioVendas', on_delete=models.CASCADE)
    dataHora = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_PAGAMENTOS)

    def __strl__(self):
            return self.status


class VendasProdutos(models.Model):
     produtoFK = models.ForeignKey(Produtos, related_name='vendasProdutos', on_delete=models.CASCADE)
     quantidade = models.IntegerField()
     vendaFK = models.ForeignKey(Vendas, related_name='vendasFK', on_delete=models.CASCADE)

     def __strl__(self):
            return self.produtoFK.nome