"""posts models"""
from django.db import models
from apps.users.models import Profile
from django.contrib.auth.models import User

class Question(models.Model):
    """Ask model"""
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="questions"
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
        return f'{self.title} by {self.profile}'


class Answer(models.Model):
    """Answer Model"""
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )
    detail_answer = models.TextField(
        blank=False
    )
    is_correct = models.BooleanField(
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
        return f'{self.title} by @{ self.profile}'
