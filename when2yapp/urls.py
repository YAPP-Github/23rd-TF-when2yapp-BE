from django.urls import include, path, re_path
from django.contrib import admin
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="ScenteTalker API",
        default_version="v1",
        description="ScenteTalker Open API 문서 페이지 입니다.",
        contact=openapi.Contact(email="bjq913@gmail.com"),
    ),
    validators=["flex"],
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # business api
    path("schedule/", include("schedule.urls")),
    # Auto DRF API docs
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
