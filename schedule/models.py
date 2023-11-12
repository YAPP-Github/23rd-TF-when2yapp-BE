from django.db import models
import datetime


class Schedule(models.Model):
    name = models.CharField(max_length=256, default="Unknown Schedule")
    url = models.URLField()
    start_date = models.DateField(default=datetime.datetime.now())
    end_date = models.DateField(default=datetime.datetime.now())
    start_time = models.TimeField(default=datetime.time(9, 0))
    end_time = models.TimeField(default=datetime.time(9, 0))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"이름: {self.name}/ 기간: {self.start_date} ~ {self.end_date}/ "
            "시간: ({self.start_time} ~ {self.end_time})"
        )


class SelectedSchedule(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    username = models.CharField(max_length=256, default="Unknown User")
    date = models.DateField(default=datetime.datetime.now())
    start_time = models.TimeField(default=datetime.time(9, 0))
    end_time = models.TimeField(default=datetime.time(9, 0))

    def __str__(self):
        return (
            f"이름: {self.username}/ 날짜: {self.date}/ "
            "시간: ({self.start_time} ~ {self.end_time})"
        )
