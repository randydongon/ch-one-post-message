from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class MessagePostManager(models.Manager):
    def get_queryset(self):
        return super(MessagePostManager, self).get_queryset().filter(status='sent')


class MessagePost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('sent', 'Sent')
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='date_send')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='message_post')
    body = models.TextField()
    date_send = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-date_send',)

    def __str__(self):
        return self.title

    objects = models.Manager()
    datesent = MessagePostManager()

    def get_absolute_url(self):
        return reverse('messageapp:detail_post', args=[self.date_send.year,
                                                       self.date_send.month,
                                                       self.date_send.day,
                                                       self.slug])
