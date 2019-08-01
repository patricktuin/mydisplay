from django.contrib import admin

from topics.models import Topic, SubTopic

admin.site.register(Topic)
admin.site.register(SubTopic)
