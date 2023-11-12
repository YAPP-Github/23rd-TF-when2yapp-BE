from .serializers import (
    ScheduleSerializer,
    SelectedScheduleSerializer,
    AvailAbilitySerializer,
)
from .models import Schedule
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


class ScheduleAPIView(APIView):
    def get_schedule(pk):
        return Schedule.objects.get(pk=pk)

    def get(self, request, pk):
        schedule = Schedule.objects.prefetch_related("selected_schedules").get(pk=pk)
        serializer = ScheduleSerializer(schedule)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        schedule = self.get_schedule(pk)
        serializer = ScheduleSerializer(schedule, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        schedule = self.get_schedule(pk)
        schedule.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ScheduleCreateAPIView(generics.CreateAPIView):
    serializer_class = ScheduleSerializer

    def post(self, request):
        """
        스케줄 생성 API

        ---
        # Body
            - name: 이름
            - start_date: 시작일
            - end_date: 종료일
            - start_time: 시작시간
            - end_time: 종료시간
        """
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class SelectedScheduleCreateAPIView(generics.CreateAPIView):
    serializer_class = SelectedScheduleSerializer

    def post(self, request, schedule_pk):
        """
        스케줄 선택 생성 API

        ---
        # Body
            - username: 사용자 이름
        """
        request_data = request.data
        request_data = {**request.data, "schedule": schedule_pk}
        print(request_data)
        serializer = SelectedScheduleSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class AvailAbilityCreateAPIView(generics.CreateAPIView):
    def post(self, request, schedule_pk, selected_schedule_pk):
        """
        가능한 스케줄 생성 API

        ---
        # Body
            - avail_abilities: 가능한 스케줄 목록
                - start_time: 시작시간
                - end_time: 종료시간
        """
        request_data = [
            {**data, "selected_schedule": selected_schedule_pk} for data in request.data
        ]

        serializer = AvailAbilitySerializer(data=request_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
