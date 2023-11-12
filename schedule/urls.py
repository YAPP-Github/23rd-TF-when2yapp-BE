from django.urls import path
from . import views

app_name = "schedule"
urlpatterns = [
    path("", views.ScheduleCreateAPIView.as_view()),
    path("<int:pk>/", views.ScheduleAPIView.as_view()),
    path("<int:schedule_pk>/selected/", views.SelectedScheduleCreateAPIView.as_view()),
    path(
        "<int:schedule_pk>/selected/<int:selected_schedule_pk>/",
        views.AvailAbilityCreateAPIView.as_view(),
    ),
]
