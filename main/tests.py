from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Volunteering


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Local Volunteer at iGV Summer by AIESEC",
            description="a six-week international exchange program promoting SDG 15: Life on Land through environmental education, community engagement, and cross-cultural collaboration.",
            category="volunteer",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Local Volunteer at iGV Summer by AIESEC")
        self.assertEqual(self.experience.category, "volunteer")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Volunteer")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

    def test_volunteering_page_is_accessible(self):
        response = self.client.get(reverse("main:show_volunteering"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "volunteering.html")

    def test_volunteering_data_is_displayed(self):
        volunteering = Volunteering.objects.create(
            title="Test Volunteering",
            description="Ini adalah volunteering untuk testing.",
            category="volunteer",
        )

        response = self.client.get(reverse("main:show_volunteering"))

        self.assertContains(response, volunteering.title)
        self.assertContains(response, volunteering.description)

    def test_empty_volunteering_page(self):
        response = self.client.get(reverse("main:show_volunteering"))
        self.assertContains(
            response,
            "Belum ada pengalaman volunteering yang ditambahkan."
        )