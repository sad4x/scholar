from django.contrib.auth.models import User
from django.db import models

class About(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    image = models.ImageField(upload_to='images/about', null=True,blank=True)

    def __str__(self):
        return self.title

class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.answer

class Course(models.Model):
    categorie = [
        ('Webdesign','Webdesign'),
        ('Development','Development'),
        ('Wordpress','Wordpress'),
    ]

    title = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()
    categories = models.CharField(max_length=30, choices=categorie)
    teacher = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/course')

    def __str__(self):
        return self.title

class Teacher(models.Model):
    image = models.ImageField(upload_to='images/teacher')
    proffesion = models.CharField(max_length=60)
    name = models.CharField(max_length=80)
    facebook = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.name

class Opinion(models.Model):
    text = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/opinion')
    proffesion = models.CharField(max_length=60)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Event(models.Model):
    categorie = [
        ('Webdesign','Webdesign'),
        ('Development','Development'),
        ('Wordpress','Wordpress'),
    ]

    title = models.CharField(max_length=80)
    date = models.DateField()
    duration = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    categorie = models.CharField(max_length=30, choices=categorie)
    img = models.ImageField(upload_to='images/event')

    def __str__(self):
        return self.title