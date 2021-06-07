from django.db import models
#from django.contrib.auth.models import User
from datetime import datetime

class Room(models.Model):
  name = models.CharField(max_length=1000)

    
class Message(models.Model):
  value = models.CharField(max_length=1000000)
  date = models.DateTimeField('date published')
  user = models.CharField(max_length=1000000)
  room = models.CharField(max_length=1000000)
  #rooms = models.ManyToManyField(User)


#class Chat(models.Model):
 # message =  models.CharField(max_length=200)
  #pub_date = models.DateTimeField('date published')
  #created = models.DateTimeField('date published')
  #updated = models.DateTimeField('date published')

  #def __str__(self):
   # return self.messege

#class Customers(models.Model):
 # from_user = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='fromuser')
  #to_user = models.ForeignKey(Chat, on_delete=models.CASCADE,  related_name='touser')
  #message =  models.CharField(max_length=200)
  #pub_date = models.DateTimeField('date published')

  #def __str__(self):
   # return self.messege

#class Question(models.Model):
  #question_text = models.CharField(max_length=200)
  #pub_date = models.DateTimeField('date published')

  #def __str__(self):
   # return self.question_text

#class Choice(models.Model):
 #   question = models.ForeignKey(Question, on_delete=models.CASCADE)
  #  choice_text = models.CharField(max_length=200)
   # votes = models.IntegerField(default=0)

    #def __str__(self):
     # return self.choice_text

