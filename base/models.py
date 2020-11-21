from django.db import models
from django.utils.text import slugify
from django.conf import settings

# Create your models here.

class Role(models.Model):
    name= models.CharField(max_length=60)

    def __str__(self):
        return self.name

class User(models.Model):
    name= models.CharField(max_length=60)
    role= models.ForeignKey(Role, related_name='fk_User_Role', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Directory(models.Model):
    name= models.CharField(max_length=100)
    slug= models.CharField(max_length=120, null=True, blank=True)
    readable= models.BooleanField(default=True)
    writable= models.BooleanField(default=True)
    user= models.ForeignKey(User, related_name='fk_Directory_User', on_delete=models.SET_NULL, null=True, blank=True)
    belongs_to= models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)

        has_slug = Directory.objects.filter(slug=slug).exists()
        count = 1
        while has_slug:
            count += 1
            slug = slugify(self.name) + '-' + str(count)
            has_slug = Directory.objects.filter(slug=slug).exists()

        self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class File(models.Model):
    name= models.CharField(max_length=100)
    slug= models.CharField(max_length=1020, null=True, blank=True)
    readable= models.BooleanField(default=True)
    writable= models.BooleanField(default=True)
    content= models.TextField(null=True, blank=True)
    user= models.ForeignKey(User, related_name='fk_File_User', on_delete=models.SET_NULL, null=True)
    belongs_to= models.ForeignKey(Directory, related_name='fk_File_Directory', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)

        has_slug = File.objects.filter(slug=slug).exists()
        count = 1
        while has_slug:
            count += 1
            slug = slugify(self.name) + '-' + str(count)
            has_slug = File.objects.filter(slug=slug).exists()

        self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


