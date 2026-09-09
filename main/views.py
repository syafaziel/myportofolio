from django.shortcuts import render

# Create your views here.
from main.models import Experience


def show_main(request):
    context = {
        "name": "Asfara Quaneisha Syafaziel",
        "npm": "2506603532",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "A first-year Information Systems student eager to develop my skills and knowledge; "
            "particularly in technology, leadership, and education. Actively seeking new opportunities and experiences <3"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Asfara Quaneisha Syafaziel",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)