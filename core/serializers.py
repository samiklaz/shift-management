import datetime

from rest_framework import serializers
from rest_framework.response import Response

from .models import *


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ('name', 'date')

    def save(self, request, *args, **kwargs):
        date = datetime.date.today()

        worker = Worker.objects.create(
            name=self.validated_data['name'],
            date=date,
        )
        worker.save()

        return worker


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftTime
        fields = ('morning', 'afternoon', 'evening', 'shift_started', 'shift_ended')

    def save(self, request, *args, **kwargs):
        morning = self.validated_data["morning"]
        afternoon = self.validated_data["afternoon"]
        evening = self.validated_data["evening"]

        array = [morning, afternoon, evening]
        count = 0
        for i in array:
            if i:
                count += 1
                print(count)

        if count == 1:
            if morning:
                shift_started = '0:00:00'
                shift_ended = '8:00:00'

            elif afternoon:
                shift_started = '8:00:00'
                shift_ended = '16:00:00'

            else:
                shift_started = '16:00:00'
                shift_ended = '23:59:00'

            shift_time = ShiftTime.objects.create(
                morning=self.validated_data['morning'],
                afternoon=self.validated_data['afternoon'],
                evening=self.validated_data['evening'],
                shift_started=shift_started,
                shift_ended=shift_ended,
            )
            shift_time.save()

            return shift_time
        else:
            raise serializers.ValidationError({"error": "You can't have two shifts in a day"})


class ShiftsGETSerializer(serializers.ModelSerializer):
    worker = WorkerSerializer()
    shift_time = TimeSerializer()

    class Meta:
        model = Shift
        fields = ('shift_set', 'worker', 'shift_time')

    def save(self, request, *args, **kwargs):
        shift = Shift.objects.create(
            shift_set=self.validated_data['shift_set'],
        )
        shift.save()

        return shift


class ShiftsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shift
        fields = ('shift_set',)

    def save(self, request, *args, **kwargs):
        shift_set = True

        shift = Shift.objects.create(
            shift_set=shift_set,
        )
        shift.save()

        return shift
