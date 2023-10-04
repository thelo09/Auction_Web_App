from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    live_until = models.DateTimeField()
    current_time = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_item.jpg', upload_to='item_pics')
    base_price = models.IntegerField(default=0)
    current_price = models.IntegerField(default=0)
    highest_bidder = models.CharField(max_length=100, default="None")

    def save(self, *args, **kwargs):
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        if self.current_price == 0:
            self.current_price = self.base_price
            # self.save()
        
        # if self.live_until:
        #     self.live_until = timezone.localtime(self.live_until, timezone=timezone.get_timezone('Asia/Kolkata'))

        super(Products, self).save(*args, **kwargs)
  
    def get_absolute_url(self):
      return reverse('auction-home')
