from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=255)
    img = models.ImageField(upload_to='banner_photo/')

    def __str__(self):
        return self.title


class Info(models.Model):
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    start_time = models.TimeField()
    end_time = models.TimeField()
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)


class About(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=255)
    img = models.ImageField(upload_to='banner_photo/')

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="service_icon/")
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Meal(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    img = models.ImageField(upload_to='meal_photos/')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    icon = models.ImageField(upload_to='test/')
    name = models.CharField(max_length=255)
    number =models.IntegerField()

    def __str__(self):
        return self.name


class Client(models.Model):
    photo = models.ImageField(upload_to='client_photos/')


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    message = models.TextField()














