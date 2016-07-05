
# Create your models here.
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200) # CharField(caracter) tipo do atributo que ele vai aceitar, no maximo letras ou numeros 200
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now) # ele vai acitar datas e vai captuar data atual
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now() # pega a data atual e mandando salvar
        self.save()

    def __str__(self): # para o administrador vizulair ou se organizar
        return self.title  # trazendo o titulo