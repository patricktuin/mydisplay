from django.contrib.auth.models import User
from django.db import models

# from displays.models import Display

from topics.models import Topic


class CustomerDisplaySetting(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topic_line')
    # line = models.CharField(max_length=8, choices=CHOICES)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    # display = models.ManyToManyField(Display, related_name='displays')

    # class Meta:
    #     unique_together = ('user', 'display',)

    # display_settings = models.ManyToManyField(CustomerDisplaySetting)

    def __str__(self):
        return self.user.username
