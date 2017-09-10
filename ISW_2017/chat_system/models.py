from django.contrib.auth.models import User
from django.db import models
from authentication import models


class Chat(models.model):
    num_chat_members = models.IntegerField(default=2)  # determina se è un gruppo o meno
    chat_members = models.ForeignKey(User)


class Message(models.model):
    message_text = models.CharField(max_length=300)
    sender = models.OneToOneField(User)
    receiver = models.OneToOneField(User)
    sending_date = models.DateField('sending date')

    def __str__(self):
        return self.message_text
