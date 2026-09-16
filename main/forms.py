from django.forms import ModelForm, TextInput, Textarea, URLInput
from main.models import Experience


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
            "ended_at": "Tanggal berakhirnya pengalaman"
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
            "category": TextInput(
                attrs={
                    "placeholder": "Kepanitiaan, Magang, Organisasi",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder":  "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "ended_at": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }