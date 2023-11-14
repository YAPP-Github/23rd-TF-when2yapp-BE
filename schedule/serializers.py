from .models import Schedule, SelectedSchedule, AvailAbility
from rest_framework import serializers


class AvailAbilitySerializer(serializers.ModelSerializer):
    selected_schedule_id = serializers.PrimaryKeyRelatedField(
        source="selected_schedule", read_only=True
    )

    class Meta:
        model = AvailAbility
        fields = ["id", "selected_schedule_id", "start_time", "end_time"]


class SelectedScheduleSerializer(serializers.ModelSerializer):
    avail_abilities = AvailAbilitySerializer(many=True, read_only=True)
    schedule_id = serializers.PrimaryKeyRelatedField(source="schedule", read_only=True)

    class Meta:
        model = SelectedSchedule
        fields = ["id", "schedule_id", "username", "avail_abilities"]


class ScheduleSerializer(serializers.ModelSerializer):
    selected_schedules = SelectedScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Schedule
        fields = [
            "id",
            "name",
            "start_date",
            "end_date",
            "start_time",
            "end_time",
            "created_at",
            "updated_at",
            "selected_schedules",
        ]
