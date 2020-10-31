from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm #new
from django.views.generic import ListView #new


class Category(models.Model):

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name = "Category"
        verbose_name_plural = "Categories" 
        unique_together = ('slug', 'parent')    

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    #meta_keywords = models.CharField('''Meta Keywords''', max_length=255)
    #meta_description = models.CharField("Meta Description", max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.PROTECT)


    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    class Meta:           
        db_table = 'products'           
        ordering = ['-created_at'] 

    name = models.CharField(max_length=255, unique=True)    
    description = models.TextField()  
    slug = models.SlugField(max_length=255, unique=True)      
    sku = models.CharField(max_length=50)      
    price = models.DecimalField(max_digits=9,decimal_places=2)       
    image = models.ImageField(upload_to='post_image', null=True, blank=True)
    is_active = models.BooleanField(default=True)           
    quantity = models.IntegerField()         
    #meta_keywords = models.CharField(max_length=255)      
    #meta_description = models.CharField(max_length=255)      
    created_at = models.DateTimeField(auto_now_add=True)      
    updated_at = models.DateTimeField(auto_now=True)      
    category = models.ManyToManyField(Category)
    is_bestseller = models.BooleanField(default=False) 
    favorite = models.ManyToManyField(User, related_name='favorite', default=None, blank=True)


    def __str__(self):           
        return self.name 


    def get_absolute_url(self):
        return reverse(
                'product_slug', 
                args=[self.slug, self.version_number]) 



class ProductReview(models.Model):
    product = models.ForeignKey(Product,blank=True, null=True ,related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User,blank=True, null=True ,related_name='reviews', on_delete=models.CASCADE)
    subject = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)      
    updated_at = models.DateTimeField(auto_now=True)