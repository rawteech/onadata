from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from main.models import UserProfile

# do not inherit from MainTestCase because we don't want auto login
class TestUserProfile(TestCase):
    def setup(self):
        self.client = Client()
        self.assertEqual(len(User.objects.all()), 0)

    def _login_user_and_profile(self, extra_post_data={}):
        post_data = {
            'username': 'bob',
            'email': 'bob@columbia.edu',
            'password1': 'bobbob',
            'password2': 'bobbob',
            'name': 'Bob',
            'city': 'Bobville',
            'country': 'US',
            'organization': 'Bob Inc.',
            'home_page': 'bob.com',
            'twitter': 'boberama'
        }
        url = '/accounts/register/'
        self.response = self.client.post(url, dict(post_data.items() + extra_post_data.items()))

    def test_create_user_with_given_name(self):
        self._login_user_and_profile()
        self.assertEqual(User.objects.all()[0].username, 'bob')

    def test_create_user_profile_for_user(self):
        self._login_user_and_profile()
        profile = User.objects.all()[0].profile
        self.assertEqual(profile.city, 'Bobville')

