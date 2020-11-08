from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    #autor
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #titulo
    title = models.CharField(max_length=200)
    #texto
    text = models.TextField()
    #fecha de creacion
    created_date = models.DateTimeField(
        default=timezone.now
    )
    #fecha de publicacuion
    published_date = models.DateTimeField(
        blank=True, null=True
    )
    #publicar
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title