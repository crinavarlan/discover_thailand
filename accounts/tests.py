from .forms import UserRegistrationForm
from django.test import TestCase
from django import forms


class CustomUserTest(TestCase):
    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'tester@test.com',
            'password1': 'test123',
            'password2': 'test123',
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'password1': 'test123',
            'password2': 'test123',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())

    def test_registration_fails_with_empty_password1(self):
        form = UserRegistrationForm({
            'email': 'tester@test.com',
            'password2': 'test123',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_registration_fails_with_empty_password2(self):
        form = UserRegistrationForm({
            'email': 'tester@test.com',
            'password1': 'test123',
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())