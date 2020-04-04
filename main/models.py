from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class MyMessagesManager(models.Manager):
#     def getserializer_data(self):
#         qs=self.get_queryset()
#         return [i.aserializer() for i in qs]
#
#
# class MyMessages(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
#     messages=models.ManyToManyField('Message',blank=True,null=True)
#     create=models.DateTimeField(auto_now=True)
#     objects=MyMessagesManager()
#     # def __str__(self):
#     #     return self.user.username
#     def aserializer(self):
#         messages=self.messages.all()
#         return {
#         'user':self.user.username,
#         'messages':[m.aserializer() for m in messages],
#         }
#
# class MessageManager(models.Manager):
#     def getAllSeriallizeData(self):
#
#         qs=self.get_queryset()
#         # if user:
#         #     qs=qs.filter()
#         return [item.aserializer() for item in qs]
#
#
# class Message(models.Model):
#                         #verbos_name , max_length
#     text=models.CharField('message',max_length=500)
#     create=models.DateTimeField(auto_now_add=True)
#     objects=MessageManager()
#     # auto_now_add - updates the value with the time and date of creation of record.
#     def aserializer(self):
#         return {
#         'text':self.text,
#         'create':str(self.create.date())
#         }
#     class Meta:
#         ordering = ['-id']


class  Country(models.Model):
    country_name=models.CharField(max_length=250,null=True)
    total_cases=models.CharField(max_length=250,null=True)
    total_death=models.CharField(max_length=250,null=True)
    total_recover=models.CharField(max_length=250,null=True)
    active_cases=models.CharField(max_length=250,null=True)
    total_case_per_minion_pop=models.CharField(max_length=250,null=True)
    total_death_per_minion_pop=models.CharField(max_length=250,null=True)
    create=models.DateField(auto_now=True,db_index=True)
    new_cases=models.ManyToManyField('NewCases',related_name="newcases")
    new_case=models.IntegerField(blank=True,default=0)
    new_death=models.IntegerField(blank=True,default=0)
    class Meta:
            ordering = ['-new_case','-new_death']
    def __str__(self):
        return self.country_name

class NewCases(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    new_cases=models.IntegerField()
    new_death=models.IntegerField()
    date=models.DateField(auto_now=True,db_index=True)
    class Meta:
            ordering = ['-date']
    def  __str__(self):
        return str(self.country)
