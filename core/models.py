from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True
    
     
        
class Category(BaseModel):
    title = models.CharField(max_length=250)
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    def __str__(self):
        return self.title
    
    
    
class Setting(BaseModel):
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logo")
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    bgimg = models.ImageField(upload_to="bgimg")
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = _("Setting")
        verbose_name_plural = _("Settings")
    
    def __str__(self):
        return self.title
    
    
     
class News(BaseModel):
    title = models.CharField(max_length=250)
    content = RichTextField()
    image = models.ImageField(upload_to="news", null=True, blank=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="news") 
      
    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        
    def __str__(self):
        return self.title
    
        


class Brands(BaseModel):
    title = models.CharField(max_length=250)
    
    
    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
        
    def __str__(self):
        return self.title
    
    
    
class Size(BaseModel):
    title = models.CharField(max_length=250)
    
    class Meta:
        verbose_name = _("Size")
        verbose_name_plural = _("Sizes")
        
    def __str__(self):
        return self.title
    

class Tag(BaseModel):
    title = models.CharField(max_length=250)
    
    
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        
    # def __str__(self):
    #     return self.title


  
class Color(BaseModel):
    title = models.CharField(null=True, blank=True)
    
    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colores")
        
    def __str__(self):
        return self.title
    







class Product(BaseModel):
    title = models.CharField(max_length=250)
    content = RichTextField()
    image = models.ImageField(upload_to="news", null=True, blank=True)
    image_2 = models.ImageField(upload_to="news", null=True, blank=True)
    image_3 = models.ImageField(upload_to="news", null=True, blank=True)
    image_4 = models.ImageField(upload_to="news", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    brands = models.ForeignKey(Brands,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag,on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="products") 
    slug = models.SlugField(unique=True, blank=True)
    # history = HistoricalRecords()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title}")
        super().save(*args, **kwargs)

    @property
    def discounted_price(self):
        return self.price * (1 - self.discount)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        
    def __str__(self):
           return self.title











class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
        
    def __str__(self):
           return self.name






class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    town_city = models.CharField(max_length=100)
    country_state = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    account_password = models.CharField(max_length=100)  # You might want to use a more secure way to store passwords
    order_notes = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"







class Subscriber(BaseModel):
    
    email = models.EmailField()
    
    class Meta:
        verbose_name = _("Subscriber")
        verbose_name_plural = _("Subscribers")
        
    def __str__(self):
           return self.email



class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')

    class Meta:
        verbose_name = _("Blogpost")
        verbose_name_plural = _("Blogposts")
        
    def __str__(self):
           return self.title



class ContactInfo(models.Model):
    country = models.CharField(max_length=100)
    content = models.TextField()
    address = models.TextField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.country
    
    class Meta:
        verbose_name = _("ContactInfo")
        verbose_name_plural = _("ContactInfos")
    
    

class AboutItem(models.Model):
    image1 = models.ImageField(upload_to='about_images/')
    question = models.CharField(max_length=255)
    answer = models.TextField()
    author = models.CharField(max_length=100)
    image2 = models.ImageField(upload_to='about_images/')
    description = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'About Item'
        verbose_name_plural = 'About Items'



class Slider(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='slider_images/')

    def __str__(self):
        return self.title1