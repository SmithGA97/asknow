"""posts models"""
from django.db import models
from apps.users.models import Profile
from django.contrib.auth.models import User

class Question(models.Model):
    """Ask model"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255
    )
    photo = models.ImageField(
        upload_to='posts/photos',
    )
    detail_question = models.TextField(
        blank=False
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return '{} by @{}'.format(self.title, self.user.username)

class Answer(models.Model):
    """Answer Model"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    question_id = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    detail_answer = models.TextField(
        blank=False
    )
    correct = models.BooleanField(
        blank=True,
        null=True
    )
    likes = models.PositiveIntegerField(null=True)
    dislikes = models.PositiveIntegerField(null=True)
    created = models.DateTimeField(
        auto_now_add=True
    )
    modified = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return '{} by @{}'.format(self.title, self.user.username)
