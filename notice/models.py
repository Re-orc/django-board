from django.db import models
from django.conf import settings

# Create your models here.
class Board(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    file = models.FileField()
    createtime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def delete(self,*args,**kwargs):
        self.file.delete()
        return super().delete(*args,**kwargs)
