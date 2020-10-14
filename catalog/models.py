from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm #new


class Category(models.Model):

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name = "Category"
        verbose_name_plural = "Categories" # doesnt seem to work?
        unique_together = ('slug', 'parent')    

    name = models.CharField(max_length=50)
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



class Meta:
    db_table = 'categories'
    ordering = ['-created_at']
    verbose_name = "Category"
    verbose_name_plural = "Categories" # doesnt seem to work?
    unique_together = ('slug', 'parent')    



#def get_absolute_url(self):      
  #  return ('catalog_category', (), { 'category_slug': self.slug }) 

#get_absolute_url = models.permalink(get_absolute_url) 

def get_absolute_url(self):
    return reverse(
            'category_slug', 
            args=[self.slug, self.version_number]) 


class Product(models.Model):

    class Meta:           
        db_table = 'products'           
        ordering = ['-created_at'] 

    #category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, unique=True)    
    description = models.TextField()  
    slug = models.SlugField(max_length=255, unique=True)      
    sku = models.CharField(max_length=50)      
    price = models.DecimalField(max_digits=9,decimal_places=2)       
    image = models.CharField(max_length=50)         
    #image_url = models.URLField(max_length=1024, null=True, blank=True) 
    image = models.FileField(upload_to='post_image', blank=True)
    #image = models.ImageField(upload_to='images', blank=True)
    is_active = models.BooleanField(default=True)           
    quantity = models.IntegerField()         
    #meta_keywords = models.CharField(max_length=255)      
    #meta_description = models.CharField(max_length=255)      
    created_at = models.DateTimeField(auto_now_add=True)      
    updated_at = models.DateTimeField(auto_now=True)      
    category = models.ManyToManyField(Category)
    is_bestseller = models.BooleanField(default=False) 



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
    stars = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)      
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.subject

