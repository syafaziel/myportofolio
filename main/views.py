from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
from main.models import Experience, Volunteering
from main.forms import ExperienceForm, VolunteeringForm


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

def create_volunteering(request):
    form = VolunteeringForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Volunteering berhasil ditambahkan!")
            return redirect("main:show_volunteering")

    context = {
        "name": "Asfara Quaneisha Syafaziel",
        "form": form,
    }

    return render(request, "volunteering_form.html", context)


def update_volunteering(request, volunteering_id):
    volunteering = get_object_or_404(Volunteering, pk=volunteering_id)

    form = VolunteeringForm(
        request.POST or None,
        instance=volunteering
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Volunteering berhasil diperbarui!")
            return redirect("main:show_volunteering")

    context = {
        "name": "Asfara Quaneisha Syafaziel",
        "form": form,
        "volunteering": volunteering,
    }

    return render(request, "volunteering_form.html", context)


def delete_volunteering(request, volunteering_id):
    volunteering = get_object_or_404(
        Volunteering,
        pk=volunteering_id
    )

    if request.method == "POST":
        volunteering.delete()
        messages.success(request, "Volunteering berhasil dihapus!")

    return redirect("main:show_volunteering")


def get_volunteering_json(request):
    title_query = request.GET.get("title", "").strip()

    volunteering = Volunteering.objects.all()

    if title_query:
        volunteering = volunteering.filter(
            title__icontains=title_query
        )

    volunteering_json = serializers.serialize(
        "json",
        volunteering
    )

    return HttpResponse(
        volunteering_json,
        content_type="application/json"
    )


def show_volunteering(request):
    json_response = get_volunteering_json(request)

    volunteering = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8")
    )

    volunteering = [
        item.object
        for item in volunteering
    ]

    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Asfara Quaneisha Syafaziel",
        "volunteer_list": volunteering,
        "title_query": title_query,
    }

    return render(
        request,
        "volunteering.html",
        context
    )