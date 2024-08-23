from django.db import models

# Create your models Flan here.

# Crear clase flan y sus campos


class Flan(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    shortName = models.SlugField()
    is_private = models.BooleanField()


def __str__(self):
    return self.name


# crear contactFrom

class ContactForm(models.Model):
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_email
    
