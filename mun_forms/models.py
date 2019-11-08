from django.db import models


class ApplicationFormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    dob = models.DateField()
    institution = models.CharField(max_length=100)
    mun_exp = models.CharField(max_length=100)
    council_p1 = models.CharField(max_length=100)
    council_p2 = models.CharField(max_length=100)
    imp_p1 = models.CharField(max_length=1500)
    q1 = models.CharField(max_length=5000)
    q2 = models.CharField(max_length=5000)
    accommodation = models.CharField(max_length=100)
