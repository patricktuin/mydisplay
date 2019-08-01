from django.db import models


class Topic(models.Model):
    topic = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.topic


class SubTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='subtopic')
    subtopic = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.subtopic
