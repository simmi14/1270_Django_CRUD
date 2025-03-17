from django.db import models

# Create your models here.


class EmpDetails(models.Model):
    emp_name = models.CharField(max_length=50)

    emp_city = models.CharField(max_length=25)

    emp_company = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.emp_name}  {self.emp_city}  {self.emp_company}"


class Album(models.Model):
    title = models.CharField(max_length=100)

    artist = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} {self.artist}"
    class meta:
        db_table="album"


class Song(models.Model):
    title = models.CharField(max_length=100)

    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    class meta:
        db_table="song"