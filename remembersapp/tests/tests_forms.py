from django.test import TestCase

from remembersapp.forms import RememberAddForm


class RememberAddFormTest(TestCase):
    def test_add_form_title_field_label(self):
        form = RememberAddForm()
        self.assertTrue(
            form.fields['title'].label is None or form.fields['title'].label == 'title')

    def test_add_form_description_field_label(self):
        form = RememberAddForm()
        self.assertTrue(
            form.fields['description'].label is None or form.fields['description'].label == 'description')

    def test_add_form_latitude_field_label(self):
        form = RememberAddForm()
        self.assertTrue(
            form.fields['latitude'].label is None or form.fields['latitude'].label == 'latitude')

    def test_add_form_longitude_field_label(self):
        form = RememberAddForm()
        self.assertTrue(
            form.fields['longitude'].label is None or form.fields['longitude'].label == 'longitude')
