from django.forms import ModelForm, TextInput, Textarea, URLInput
from main.models import Experience, Volunteering
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Nama Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "thumbnail": "Gambar Pengalaman",
            "ended_at": "Tanggal berakhirnya pengalaman",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Pengalamanmu",
                    "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }


class VolunteeringForm(ModelForm):
    class Meta:
        model = Volunteering
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Nama Volunteering",
            "description": "Deskripsi Volunteering",
            "category": "Kategori Volunteering",
            "thumbnail": "Gambar Volunteering",
            "ended_at": "Tanggal Berakhirnya Volunteering",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Nama Volunteering",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalaman volunteeringmu",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "Volunteer",
                    "maxlength": 20,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()

        if not title:
            raise ValidationError(
                "Nama volunteering tidak boleh hanya berisi tag HTML."
            )

        return title


    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()


    def clean_category(self):
        return strip_tags(self.cleaned_data["category"]).strip()