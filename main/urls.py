from django.urls import path

from main.views import (
    show_main,
    show_experience,
    show_volunteering,
    create_experience,
    get_experience_json,
    delete_experience,
    create_volunteering,
    update_volunteering,
    delete_volunteering,
    get_volunteering_json,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),

    # Experience
    path(
        "experience/",
        show_experience,
        name="show_experience"
    ),
    path(
        "experience/add/",
        create_experience,
        name="create_experience"
    ),
    path(
        "api/experience/",
        get_experience_json,
        name="get_experience_json"
    ),
    path(
        "experience/<uuid:experience_id>/delete/",
        delete_experience,
        name="delete_experience"
    ),

    # Volunteering
    path(
        "volunteering/",
        show_volunteering,
        name="show_volunteering"
    ),
    path(
        "volunteering/add/",
        create_volunteering,
        name="create_volunteering"
    ),
    path(
        "volunteering/<uuid:volunteering_id>/edit/",
        update_volunteering,
        name="update_volunteering"
    ),
    path(
        "volunteering/<uuid:volunteering_id>/delete/",
        delete_volunteering,
        name="delete_volunteering"
    ),
    path(
        "api/volunteering/",
        get_volunteering_json,
        name="get_volunteering_json"
    ),
]