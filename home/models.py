from django.db import models

# Create your models here.
class NewsletterSignup(models.Model):
    email = models.EmailField()
    #has_verified = models.BooleanField()
    # hash = models.CharField() 

    def __str__(self):
        return self.email