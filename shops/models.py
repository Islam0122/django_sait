from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    create_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    img = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=24)
    description = models.TextField(blank=True, null=True)
    rate = models.FloatField()
    prize = models.FloatField(max_length=1000000)
    create_data = models.DateTimeField(auto_now_add=True)
    modified_data = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    phone_number = models.FloatField()


    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text}-> {self.product.title}'

