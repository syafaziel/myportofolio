from django.forms import ModelForm, TextInput, Textarea, URLInput
from main.models import Experience, Volunteering


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
            "ended_at": "Tanggal berakhirnya volunteering",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "BRIDGE by Girl Up UI",
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