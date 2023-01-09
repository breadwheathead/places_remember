from django.test import TestCase
from django.urls import reverse

from mainapp.models import User
from remembersapp.models import Remember


class RememberListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='firebrand', password='qwerty')
        number_of_remembers = 12
        for num in range(number_of_remembers):
            Remember.objects.create(
                user=user,
                title=f'Кафе №{num}',
                description=f'{num} атмосферное заведение',
                latitude=float(num),
                longitude=float(num)
            )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get('/remembers/')
        self.assertRedirects(response, '/?next=/remembers/')

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='firebrand', password='qwerty')
        response = self.client.get('/remembers/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='firebrand', password='qwerty')
        response = self.client.get(reverse('remembers:remembers'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='firebrand', password='qwerty')
        response = self.client.get(reverse('remembers:remembers'))
        self.assertTemplateUsed(response, 'remembersapp/remembers.html')

    def test_pagination_is_ten(self):
        self.client.login(username='firebrand', password='qwerty')
        response = self.client.get(reverse('remembers:remembers'))
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] is True)
        self.assertTrue(len(response.context['page_obj']) == 10)

    def test_lists_all_remembers(self):
        self.client.login(username='firebrand', password='qwerty')
        response = self.client.get(reverse('remembers:remembers') + '?page=2')
        self.assertTrue(len(response.context['page_obj']) == 2)

    def test_logged(self):
        self.client.login(username='firebrand', password='qwerty')
        response = self.client.get(reverse('remembers:remembers'))
        self.assertEqual(str(response.context['user']), 'firebrand')
        self.assertEqual(response.status_code, 200)

    def test_only_remembers_by_current_user(self):
        self.client.login(username='firebrand', password='qwerty')
        response = self.client.get(reverse('remembers:remembers'))
        self.assertTrue('object_list' in response.context)
        for remember in response.context['object_list']:
            self.assertEqual(response.context['user'], remember.user)
