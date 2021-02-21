from django.db import models

# Create your models here.


class Dojo(models.Model):
    # FIELD NAMES GO HERE
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"<Dojo objects: {self.name} ({self.id})"

# THE TABLE THAT HAS THE MANY IN THE ONE TO MANY RELATIONSHIP IS THE ONE THAT WILL HAVE THE FOREIGN KEY


class Ninja(models.Model):
    # FIELD NAMES GO HERE
    # STUDENTS IS REFERRING TO THE DATA COLLECTED FROM CLASS DOJO
    assigneddojo = models.ForeignKey(
        Dojo, related_name="students", on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Dojo(models.Model):
#     # FIELD NAMES GO HERE
#     fname = models.CharField(max_length=255)
#     lname = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     age = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
# ------------------------------------------------------------------
# from django.db import models
# class Movie(models.Model):
#     title = models.CharField(max_length=45)
#     description = models.TextField()
#     release_date = models.DateTimeField()
#     duration = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
