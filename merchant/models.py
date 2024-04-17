import hashlib
import random
import string

from django.db import models


class Application(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=12)  # maybe the "phonenumber_field" plugin can be used.
    token = models.CharField(max_length=32, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.token:
            random_stirng = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(32))
            data_to_hash = f"{self.email}_{self.first_name}_{random_stirng}"
            self.token = hashlib.md5(data_to_hash.encode()).hexdigest()
            
        super().save(*args, **kwargs)        
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.token})"


class Channel(models.Model):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    website_url = models.URLField(max_length=254)
    trendyol_url = models.URLField(max_length=254)
    amazon_url = models.URLField(max_length=254)
    
    def __str__(self) -> str:
        return f"{self.application.first_name} {self.application.last_name} ({self.application.token})"