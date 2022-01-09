from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')
    
    # Objeto estânciado de acordo com o que a gente quer
    def __str__(self):
        return self.nome
    

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email =  models.EmailField('E-mail', max_length=100)
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
    