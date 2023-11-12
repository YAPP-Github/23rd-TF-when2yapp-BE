from django.db import models
import datetime
from django.utils import timezone


class Schedule(models.Model):
    name = models.CharField(max_length=256, default="Unknown Schedule")
    hash_value = models.CharField(max_length=256)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    start_time = models.TimeField(default=datetime.time(9, 0))
    end_time = models.TimeField(default=datetime.time(9, 0))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"이름: {self.name}/ 기간: {self.start_date} ~ {self.end_date}/ "
            f"시간: ({self.start_time} ~ {self.end_time})"
        )


class SelectedSchedule(models.Model):
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        related_name="selected_schedules",
        null=False,
    )
    username = models.CharField(max_length=256, default="Unknown User")

    def __str__(self):
        return f"스케줄명: {self.schedule.name}/ 사용자명: {self.username}"


class AvailAbility(models.Model):
    selected_schedule = models.ForeignKey(
        SelectedSchedule,
        on_delete=models.CASCADE,
        related_name="avail_abilities",
        null=False,
    )
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return (
            f"스케줄명: {self.selected_schedule.schedule.name}/ "
            f"사용자명: {self.selected_schedule.username}/ "
            f"시작: {self.start_time}/ 끝: {self.end_time}"
        )
