from django.test import TestCase

from mainapp.models import User
from remembersapp.models import Remember
from remembersapp.forms import RememberAddForm


class RememberModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='firebrand')
        Remember.objects.create(
            user=user,
            title='Кафе Мелодия',
            description='Уютное атмосферное заведение',
            latitude='55.9662',
            longitude='92.8309'
        )

    def test_title_label(self):
        remember = Remember.objects.get(id=1)
        field_label = remember._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_description_label(self):
        remember = Remember.objects.get(id=1)
        field_label = remember._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_latitude_label(self):
        remember = Remember.objects.get(id=1)
        field_label = remember._meta.get_field('latitude').verbose_name
        self.assertEquals(field_label, 'latitude')

    def test_longitude_label(self):
        remember = Remember.objects.get(id=1)
        field_label = remember._meta.get_field('longitude').verbose_name
        self.assertEquals(field_label, 'longitude')

    def test_title_max_length(self):
        remember = Remember.objects.get(id=1)
        max_length = remember._meta.get_field('title').max_length
        self.assertEquals(max_length, 128)

    def test_description_max_length(self):
        remember = Remember.objects.get(id=1)
        max_length = remember._meta.get_field('description').max_length
        self.assertEquals(max_length, 512)

    def test_object_name_is_title(self):
        remember = Remember.objects.get(id=1)
        expected_object_name = remember.title
        self.assertEquals(expected_object_name, str(remember))


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
