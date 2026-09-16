from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
from main.models import Experience, Volunteering
from main.forms import ExperienceForm


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

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Experience berhasil ditambahkan!")
            return redirect("main:show_experience")

    context = {
        "name": "Asfara Quaneisha Syafaziel",
        "form": form,
    }

    return render(request, "experience_form.html", context)

def show_volunteering(request):
    context = {
        "name": "Asfara Quaneisha Syafaziel",
        "volunteer_list": Volunteering.objects.all(),
    }
    return render(request, "volunteering.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Asfara Quaneisha Syafaziel",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")