from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class IndexAPIView(APIView):
    def get(self, request):
        shifts = Shift.objects.all()
        serializer = ShiftsGETSerializer(shifts, many=True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data['name']
        date = datetime.date.today()

        try:
            query = Worker.objects.get(name=name, date=date)

            if query.date == date:
                data = {
                    "response": "error",
                    "message": "you can't have two shifts on the same day"
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            else:
                worker_serializer = WorkerSerializer(data=request.data)
                time_serializer = TimeSerializer(data=request.data)
                shift_serializer = ShiftsSerializer(data=request.data)

                if worker_serializer.is_valid():
                    if time_serializer.is_valid():

                        if shift_serializer.is_valid():
                            worker = worker_serializer.save(False)
                            shift_time = time_serializer.save(False)
                            shift = shift_serializer.save(False)

                            shift.worker = worker
                            shift.shift_time = shift_time

                            worker.save()
                            shift_time.save()
                            shift.save()
                            data = {
                                "response": "successful",
                                "message": "your shift have been created successfully"
                            }
                            return Response(data, status=status.HTTP_200_OK)

                        return Response(shift_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                    return Response(time_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response(worker_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            worker_serializer = WorkerSerializer(data=request.data)
            time_serializer = TimeSerializer(data=request.data)
            shift_serializer = ShiftsSerializer(data=request.data)

            if worker_serializer.is_valid():
                if time_serializer.is_valid():

                    if shift_serializer.is_valid():
                        worker = worker_serializer.save(False)
                        shift_time = time_serializer.save(False)
                        shift = shift_serializer.save(False)

                        shift.worker = worker
                        shift.shift_time = shift_time

                        worker.save()
                        shift_time.save()
                        shift.save()
                        data = {
                            "response": "successful",
                            "message": "your shift have been created successfully"
                        }
                        return Response(data, status=status.HTTP_200_OK)

                    return Response(shift_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                return Response(time_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(worker_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



