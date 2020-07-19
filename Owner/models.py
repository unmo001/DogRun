from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Owner(AbstractBaseUser):
    class Meta:
        db_table = 'owner'

    username = models.CharField(verbose_name='名前', max_length=255, unique=True)
    email = models.EmailField(verbose_name='Eメール', max_length=255)
    age = models.IntegerField(verbose_name='年齢', null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    picture = models.ImageField(upload_to='images/')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
#
# class Dog(models.Model):
#
#     mele = 'オス'
#     femele = 'メス'
#
#     sex_choice = {
#         (mele, 'オス'),
#         (femele, 'メス'),
#     }
#
#     class Meta:
#         db_table = 'dog'
#
#     name = models.CharField(verbose_name='名前',max_length=255)
#     age = models.IntegerField(verbose_name='年齢', null=False, blank=False)
#     sex = models.CharField(choice=sex_choice)
