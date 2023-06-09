from django.db import models
from django.shortcuts import redirect


class user(models.Model):
    uid= models.CharField(max_length=20)
    uname=models.CharField(max_length=100)
    uemail=models.EmailField()
    ucontact=models.CharField(max_length=20)

    class Meta:
        db_table ='user'

class Userdata(models.Model):

    Name=models.CharField(max_length=45)
    Email=models.EmailField()
    PhoneNo = models.CharField(max_length=35)
    Message=models.CharField(max_length=450)

    class Meta:
        db_table='userdata'

class Admindata(models.Model):

    UserId=models.CharField(max_length=50)
    Password=models.CharField(max_length=100)
    class Meta:
        db_table='admin_data'
class BlogData(models.Model):
    blog_title = models.CharField(max_length=255)
    blog_description = models.TextField()
    blog_img = models.ImageField(upload_to='static/blog_images/')

    class Meta:
        db_table='blogdata'

class PortfolioData(models.Model):
    portfolio_title = models.CharField(max_length=255)
    portfolio_link = models.TextField()
    portfolio_img = models.ImageField(upload_to='static/portfolio_images/')

    class Meta:
        db_table = 'portfoliodata'


class Skill(models.Model):
    skill_category = models.CharField(max_length=100)
    skill_name = models.CharField(max_length=100)
    rating = models.IntegerField()

    class Meta:
        db_table ='skills'



# Create your models here.
