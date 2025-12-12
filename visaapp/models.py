from django.db import models

# Create your models here.


class VISA(models.Model):
    C_name = models.ImageField(upload_to="images/", null=True, blank=True)
    C_number = models.IntegerField()
    C_W_number = models.CharField(max_length=110)
    C_email = models.EmailField()
    C_description = models.TextField(max_length=2000)


