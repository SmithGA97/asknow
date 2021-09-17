"""Users models"""

#Django
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Profile Model
    Proxy models that extends the base data with other information"""
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    biography = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=False)
    picture = models.ImageField(
        upload_to = 'users/pictures',
        blank = True,
        null = True
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return username"""
        return self.user.username