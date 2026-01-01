from django.db import models


# Create your models here.
class Category(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    cat_image = models.ImageField(upload_to="photos/categories/", blank=True, null=True)
=======
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    cat_image = models.ImageField(upload_to="photos/categories", blank=True, null=True)
>>>>>>> 7f5859f (update)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
<<<<<<< HEAD

    def __str__(self):
        return self.name
=======
        ordering = ["category_name"]

    def __str__(self):
        return self.category_name
>>>>>>> 7f5859f (update)
