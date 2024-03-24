from django.db import models

class Author(models.Model):
    Name = models.CharField(max_length=20,verbose_name='作者')
    email = models.EmailField()
    gender = models.BooleanField()
    def __str__(self):
        return self.Name


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=12)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=12)
    website = models.URLField()
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30)
    publish_date = models.DateField(verbose_name='出版时间')
    author = models.ForeignKey(Author,on_delete=models.CASCADE,verbose_name='作者')
    publishers = models.ManyToManyField(Publisher,verbose_name='出版社')
    def __str__(self):
        return self.title


