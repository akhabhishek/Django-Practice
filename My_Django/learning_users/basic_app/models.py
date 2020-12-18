from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    # Create relationship iwth User class (Don't inherit from User)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add additional attributes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True) # Make sure to create the profile_pics folder under media directory

    def __str__(self):
        return self.user.username
