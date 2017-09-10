from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models


# Queste modifiche alla classe User sono necessarie in quanto voglio che un utente venga identificato univocamente
# non per il suo username, ma per la sua email, e usare il campo email nel login.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', unique=True)
    name = models.CharField('name', max_length=25)
    surname = models.CharField('surname', max_length=30)
    username = models.CharField('username', max_length=20, unique=True, null=True)

    objects = UserManager()
    # identificatore unico
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Meta:
    model = User

    def get_short_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_full_name(self):
        return self.get_name() + " " + self.get_surname()

    def get_email(self):
        return self.email

