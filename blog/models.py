from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from model_utils import Choices


'''Simple Post model, all in one table. The "author" string refers to the abstract User class.'''

STATUS_CHOICES = Choices(
    ('draft', 'Draft'),
    ('published', 'Published'),
)


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True, blank=True)  # A string consisting of ASCII letters or numbers.
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})