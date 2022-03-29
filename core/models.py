from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Worker(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


CHOICES = (
    ('MORNING', 'MORNING'),
    ('AFTERNOON', 'AFTERNOON'),
    ('EVENING', 'EVENING')
)


class ShiftTime(models.Model):
    morning = models.BooleanField(default=False)
    afternoon = models.BooleanField(default=False)
    evening = models.BooleanField(default=False)
    shift_started = models.TimeField(blank=True, null=True)
    shift_ended = models.TimeField(blank=True, null=True)

    def __str__(self):
        return str(self.shift_started)


class Shift(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, blank=True, null=True)
    shift_time = models.ForeignKey(ShiftTime, on_delete=models.CASCADE, blank=True, null=True)
    shift_set = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.worker.name)



