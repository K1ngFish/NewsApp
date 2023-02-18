from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm
from django.core.mail import EmailMultiAlternatives


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


# class CustomSignupForm(SignupForm):
#     def save(self, request):
#         user = super().save(request)
#         common_users = Group.objects.get(name="users")
#         user.groups.add(common_users)
#         return user


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="users")
        user.groups.add(common_users)

        subject = 'Добро пожаловать на наш новостной сайт!'
        text = f'Здравствуйте, {user.username}! Вы успешно зарегистрировались на сайте! Рады вас видеть.'
        html = (
            f'Здравствуйте, <b>{user.username}</b>! Вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/products">сайте</a>! Рады вас видеть.'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        return user
