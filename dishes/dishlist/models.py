from django.db import models

# Create your models here.

dishes=[
    {"id":1,"name":"chicken biriyani","prize":180,"category":"non_veg"},
    {"id":2,"name":"beef biriyani","prize":200,"category":"non_veg"},
    {"id":3,"name":"payampori","prize":10,"category":"snack"},
    {"id":4,"name":"kanji","prize":80,"category":"veg"},
]

class Dishes(models.Model):
    name=models.CharField(max_length=100,null=True)
    prize=models.IntegerField(null=True)
    category=models.CharField(max_length=100,null=True)