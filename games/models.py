from django.db import models

# Create your models here.

class Games(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)
    start_date = models.DateField(blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"(id={self.id},title={self.title})"