from django.db import models

# Create your models here.
class Type(models.Model):
    type_name = models.CharField(max_length=255)
    def __str__(self):
        return self.type_name


class Classification(models.Model):
    classification_name = models.CharField(max_length=255)
    def __str__(self):
        return self.classification_name


class Port(models.Model):
    port_name = models.CharField(max_length=255)
    def __str__(self):
        return self.port_name


class Age(models.Model):
    age_name = models.CharField(max_length=255)
    def __str__(self):
        return self.age_name


class Animal(models.Model):
    animal_name = models.CharField(max_length=255)
    animal_age = models.ManyToManyField(Age)
    animal_weight = models.FloatField()
    animal_type = models.ManyToManyField(Type)
    animal_port = models.ManyToManyField(Port)
    def __str__(self):
        return self.animal_name


class User(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)
    user_animals = models.ManyToManyField(Animal)
    def __str__(self):
        return self.user_name +"/"+ self.user_email


class Attributes(models.Model):
    attributes_name = models.CharField(max_length=255)
    def __str__(self):
        return self.attributes_name


class Ration(models.Model):
    ration_name = models.CharField(max_length=255)
    ration_desc = models.TextField()
    ration_age = models.ManyToManyField(Age)
    ration_image = models.CharField(max_length=2083)
    ration_atrib = models.ManyToManyField(Attributes)
    ration_type = models.ManyToManyField(Type)
    ration_port = models.ManyToManyField(Port)
    ration_classification = models.ManyToManyField(Classification)
    ration_price = models.FloatField()
    def __str__(self):
        return self.ration_name