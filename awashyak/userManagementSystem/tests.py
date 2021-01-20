from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .views import userRegistrationSave

# Create your tests here.

class CustomeUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='abishek',
            email = 'a@gmail.com',
            password = 'testpass123'
        )

        self.assertEqual(user.username,'abishek')
        self.assertEqual(user.email,'a@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'superadmin',
            email = 'superadmin@gmail.com',
            password = 'testpass123'
        )

        self.assertEqual(admin_user.username,'superadmin')
        self.assertEqual(admin_user.email,'superadmin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class RegisterPageTests(TestCase):
    def setUp(self):
        url = reverse('register')
        self.response = self.client.get(url)

    def test_register_template(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,'register.html')
        self.assertContains(self.response,'Register')
        self.assertNotContains(self.response,'This page is not allowed to visit')


    def test_register_view(self): 
        view = resolve('/register/save/')
        self.assertEqual(
        view.func.__name__,
        userRegistrationSave.__name__
        )

class LoginTests(TestCase):

    username = 'newuser'
    email = 'newuser@gmail.com'

    def setUp(self):
        url = reverse('login')
        self.response = self.client.get(url)

    def test_login_template(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,'login.html')
        self.assertContains(self.response,'Login')

    def test_login_form(self):
        new_user = get_user_model().objects.create_user(self.username,self.email)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email,self.email)