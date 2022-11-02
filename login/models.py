from django.db import models

class terserahaja(models.Model):
    nama =models.CharField( max_length=100)

    def __str__(self) :
        return self.name