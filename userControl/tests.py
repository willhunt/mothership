from django.test import TestCase, Client
from django.core.urlresolvers import resolve, reverse
from .views import UserFormView
from django.contrib.auth.models import User
from django.contrib import auth

# HELPER FUNCTIONS -------------------------------------------------------------
def create_user(password=None):
    user = User.objects.create_user('testuser', 'testuser@testuser.com', password)
    user.first_name = 'Test'
    user.last_name = 'User'
    user.save()
    return user


# SUPERCLASS TESTS -------------------------------------------------------------
class UserTestsWithUser(TestCase):
    ''' Inherit for testing with a user logged in '''
    def setUp(self):
        # Create user
        password = 'qwerty'
        self.user = create_user(password=password)
        self.client = Client()
        self.loggedin = self.client.login(username=self.user.username, password=password)


# TESTS ------------------------------------------------------------------------
class NewUserViewTests(TestCase):

    def test_user_form_view(self):
        response = self.client.get(reverse('userControl:register'))
        # Check http response code is good
        self.assertEqual(response.status_code, 200)

    def test_user_login_view(self):
        response = self.client.get(reverse('userControl:login'))
        # Check http response code is good
        self.assertEqual(response.status_code, 200)


class CurrentUserViewTests(UserTestsWithUser):

    def test_user_is_authenticated(self):
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated())


    def test_user_logout_view(self):
        response = self.client.get(reverse('userControl:logout'))
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated())
        # Check http response code is good
        self.assertRedirects(response, reverse('main:index'))

