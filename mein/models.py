from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='banner/', null=True, blank=True)

    def __str__(self):
        return self.title


class Properties(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    number = models.IntegerField(default=0)
    logo = models.ImageField(upload_to='about_as/', null=True, blank=True)

    def __str__(self):
        return self.name


class Agent1(models.Model):
    text = models.TextField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Agent(models.Model):
    name = models.CharField(max_length=200)
    jop = models.TextField()
    photo = models.ImageField(upload_to='agent/', null=True, blank=True)
    instagram = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    google = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Agent2(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    title = models.CharField(max_length=225)
    text = models.TextField()

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    vido = models.URLField(null=True, blank=True)
    description = models.CharField(max_length=225)

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    logo = models.ImageField(upload_to='logo_services/', null=True, blank=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=225)
    jop = models.CharField(max_length=222)
    img = models.ImageField(upload_to='photo/', null=True, blank=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=225)
    text = models.TextField()
    date = models.DateTimeField()
    img = models.ImageField(upload_to='news_photo/', null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=225)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name



