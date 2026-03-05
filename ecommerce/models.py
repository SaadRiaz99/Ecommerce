from django.db import models

# Create your models here.
# class authtencate(models.Model):
#     username = Models.charField(max_length = 50 , null = False)
#     Password = Models.charField(max_length = 10 , null = False)

class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=120, null=False)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


