from django.db import models

class NavbarItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class QuienesSomos(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Servicio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
