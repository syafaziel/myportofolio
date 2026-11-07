from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    path("experiences/", api_views.experience_list, name="experience-list"),
    path("experiences/<uuid:experience_id>/", api_views.experience_detail, name="experience-detail"),
    path("experiences/<uuid:experience_id>/star/", api_views.experience_star, name="experience-star"),
    path("volunteering/", api_views.volunteering_list, name="volunteering_list"),
    path("volunteering/<uuid:id>/", api_views.volunteering_detail, name="volunteering_detail"),
    path("volunteering/<uuid:id>/star/", api_views.volunteering_star, name="volunteering_star"),
]
