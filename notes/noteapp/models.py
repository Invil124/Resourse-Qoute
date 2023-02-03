from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Author(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    born_date = models.DateTimeField(null=False)
    born_location = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.full_name}"


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='tag of username')
        ]

    def __str__(self):
        return f"{self.name}:"


class Quote(models.Model):
    author = models.ForeignKey(Author, null=False, on_delete=models.CASCADE)
    quote = models.TextField(unique=True, null=False)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.quote}: {self.author}"


