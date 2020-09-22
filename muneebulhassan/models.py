from django.db import models

# Create your models here.
class connect(models.Model):
    u_name = models.CharField(max_length=50)
    u_subject = models.CharField(max_length=100)
    u_description = models.CharField(max_length=300)


class project(models.Model):
    p_name = models.CharField(max_length=30)
    p_link = models.CharField(max_length=100)
    p_description = models.CharField(max_length=110)
    p_framework = models.CharField(max_length=50)

class experience(models.Model):
    e_name = models.CharField(max_length=30)
    e_post = models.CharField(max_length=50)
    e_startdate = models.CharField(max_length=30)
    e_enddate = models.CharField(max_length=30)
