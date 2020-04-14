from django.db import models

# Create your models here.
class Division(models.Model):
    division=models.CharField(max_length=250)
    city=models.ManyToManyField('City',related_name='city_or_district')
    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['id']
    def __str__(self):
        return self.division
class City(models.Model):
    divi=models.ForeignKey('Division',on_delete=models.CASCADE,related_name='d')
    city=models.CharField(max_length=250)
    namberofCases=models.IntegerField()
    date=models.DateTimeField()
    class Meta:
        ordering=['-namberofCases']
    def __str__(self):
        return self.city
