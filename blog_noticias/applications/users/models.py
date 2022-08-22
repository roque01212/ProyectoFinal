from django.db import models


# Create your models here.
class Users(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE,related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'About/', blank=True)

    def __str__(self):
        return self.user.username + ' - profile'

    


