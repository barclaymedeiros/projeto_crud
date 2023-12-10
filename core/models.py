from django.db import models

class Filme(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'core_filmes'