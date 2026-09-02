from django.urls import include, path

urlpatterns = [path("api/aws/", include("cloud.urls"))]

