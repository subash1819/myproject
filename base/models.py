from django.db import models

# Create your models here.
options=(
    ('MALE','male'),
    ('FEMALE','female')
)
class Item(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200,default='example@gmail.com')
    Phone=models.IntegerField(max_length=13,default='11111111')
    DOB=models.DateTimeField(auto_now_add=False)
    Location=models.CharField(max_length=100,default='India')
    Gender=models.CharField(choices=options,max_length=10,default='MALE')
    Address=models.CharField(max_length=200,default='India')
     