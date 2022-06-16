from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='images/restaurants')
    kitchen_style = models.CharField(max_length=50)
    location = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.name} - {self.location}"
