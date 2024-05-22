from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.CharField(max_length=30)
    id_user = pass
    bio = pass
    profileomg = pass


# class Author(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     birth_date = models.DateField()

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
