from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    comment=models.CharField(max_length=500)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.email}"
    class Meta:
        ordering=['-created']
