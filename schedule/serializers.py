from .models import Schedule, SelectedSchedule, AvailAbility
from rest_framework import serializers


class AvailAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailAbility
        fields = "__all__"


class SelectedScheduleSerializer(serializers.ModelSerializer):
    avail_abilities = AvailAbilitySerializer(many=True, read_only=True)

    class Meta:
        model = SelectedSchedule
        fields = ["id", "schedule", "username", "avail_abilities"]


class ScheduleSerializer(serializers.ModelSerializer):
    selected_schedules = SelectedScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Schedule
        fields = [
            "name",
            "start_date",
            "end_date",
            "start_time",
            "end_time",
            "created_at",
            "updated_at",
            "selected_schedules",
        ]
