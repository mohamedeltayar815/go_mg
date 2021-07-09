from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name


class visit(models.Model):
    n = models.CharField(max_length=50, default='patient')
    visitno = models.IntegerField(default=0)
    age = models.IntegerField()
    is_married = models.BooleanField(default=False)
    is_pregnant = models.BooleanField(default=False)
    noofbirth = models.IntegerField(default=0)
    last_birth = models.CharField(max_length=50)
    last_priod = models.CharField(max_length=50)
    medical_complaint = models.CharField(max_length=200)
    treatment = models.CharField(max_length=200)
    d = models.CharField(max_length=100)
    edfb = models.CharField(max_length=100)
    medicalhestory = models.TextField(default='clear')
    patient = models.ForeignKey(Customer, on_delete=models.CASCADE)
    important_ad = models.TextField(null=True,blank=True)
    sonar = models.ImageField(default="1234.jpg", null=True, blank=True)
    sonar01 = models.ImageField(default="1234.jpg", null=True, blank=True)
    sonar02 = models.ImageField(default="1234.jpg", null=True, blank=True)
    sonar03 = models.ImageField(default="1234.jpg", null=True, blank=True)
    lap = models.ImageField(default="1234.jpg", null=True, blank=True)
    lap01 = models.ImageField(default="1234.jpg", null=True, blank=True)

    def __str__(self):
        return self.n


class vphoto(models.Model):
    pn = models.IntegerField(default=0)
    p = models.TextField(default='.....')
    Visit = models.ForeignKey(visit, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.p


class maqal(models.Model):
    titel = models.CharField(max_length=50)
    text = models.TextField()
    pic = models.ImageField(default="1234.jpg", null=True, blank=True)
    pic2 = models.ImageField(default="1234.jpg", null=True, blank=True)
    def __str__(self):
        return self.titel

class coment(models.Model):
    coment = models.TextField()
    mit = models.ForeignKey(maqal, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{} - {}'.format(self.coment, self.mit)



class Link(models.Model):
    about = models.CharField(max_length=50, null=True, blank=True)
    link = models.TextField(null=True, blank=True)


class massage(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=50, blank=True, null=True)
    massage = models.TextField(null=True, blank=True)
    def __str__(self):
        return '{} - {}'.format(self.name, self.subject)




class vItem(models.Model):
    video = EmbedVideoField()  # same like models.URLField()
    description = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.subject



class coment1(models.Model):
    coment = models.TextField()
    vI = models.ForeignKey(vItem, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{} - {}'.format(self.coment, self.vI)



class frist(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pic = models.ImageField(default="1234.jpg", null=True, blank=True)
    pic2 = models.ImageField(default="1234.jpg", null=True, blank=True)

    def __str__(self):
        return self.name



class scond(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pic = models.ImageField(default="1234.jpg", null=True, blank=True)
    pic2 = models.ImageField(default="1234.jpg", null=True, blank=True)


    def __str__(self):
        return self.name


class third(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pic = models.ImageField(default="1234.jpg", null=True, blank=True)
    pic2 = models.ImageField(default="1234.jpg", null=True, blank=True)


    def __str__(self):
        return self.name




class fourth(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pic = models.ImageField(default="1234.jpg", null=True, blank=True)
    pic2 = models.ImageField(default="1234.jpg", null=True, blank=True)


    def __str__(self):
        return self.name


