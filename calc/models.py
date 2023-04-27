from django.db import models

class Formula(models.Model):
    x1 = models.FloatField(default=0)
    x2 = models.FloatField(default=0)
    x3 = models.FloatField(default=0)
    delta = models.FloatField(null=True)
    res1 = models.FloatField(null=True)
    res2 = models.FloatField(null=True)

    def __int__(self):
        return self.id
class Usuario(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome

