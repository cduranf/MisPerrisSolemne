from django.db import models
from django.utils import timezone


class Post(models.Model):
    ESTADO = (
        ("Espera","Espera"),
        ("Adoptado","Adoptado"),
    )

    Nombre = models.CharField(max_length=200)
    Descripcion = models.TextField()
    Estado = models.TextField(choices=ESTADO, default='Espera')
    published_date = models.DateTimeField(
            blank=True, null=True)

    picture = models.ImageField(
        upload_to='user_pics', default='default.jpg')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Nombre