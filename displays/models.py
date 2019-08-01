from django.db import models

from topics.models import Topic

from accounts.models import Customer

FONT_SIZES = ((8, 'Small'), (12, 'Normal'), (15, 'Large'))


class MyDisplayModel(models.Model):
    display_model = models.CharField(max_length=64, unique=True)
    # @TODO version number need to be unique and cannot be accepted empty
    # serial_number = models.PositiveSmallIntegerField(null=True, blank=True)
    # @TODO Add an image field?
    # @TODO lines cannot be accepted empty
    max_lines = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.display_model


class Display(models.Model):
    model = models.ForeignKey(MyDisplayModel, on_delete=models.CASCADE, related_name='model')
    serial_number = models.PositiveSmallIntegerField(unique=True)
    friendly_name = models.CharField(max_length=64, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer', blank=True, null=True)
    font_size = models.PositiveSmallIntegerField(choices=FONT_SIZES, default=12)

    def __str__(self):
        return str(self.serial_number)


class Line(models.Model):
    display = models.ForeignKey(Display, on_delete=models.CASCADE, related_name='lines')
    line = models.CharField(max_length=16)
    user_text = models.CharField(max_length=16, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.line
