from django.db import models

# Create your models here.

class Players(models.Model):
    nickname = models.CharField( max_length=50,unique=True)
    country = models.CharField( max_length=50,null=False,blank=False)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"(id={self.id},nickname={self.nickname})"