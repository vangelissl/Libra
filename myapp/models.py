from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def lifespan(self):
        return f"{self.birth_date} {self.death_date if self.death_date else ''}"

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=100)
    pages = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
