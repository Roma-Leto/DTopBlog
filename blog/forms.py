# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import BNotePost
from django.contrib.auth.decorators import login_required
# For registration users
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
## signal for registration func
# from .apps import user_registered


class RegisterUserForm(ModelForm):
    email =  EmailField(required=True, label='Адрес электронной почты')
    password1 = CharField(label='Пароль', widget=PasswordInput, 
                          help_text=password_validation.password_validators_help_text_html())
    password2 = CharField(label='Пароль (повторно)', widget=PasswordInput,
                          help_text="Повторите пароль.")

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password('password1')
        return password1

    def clean(self):
        super().clean()
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Пароли не совпадают', 
                    code='password_mismatch')}
                raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        user_registered.send(RegisterUserForm, instanse=user)
        return user

    class Meta:
        model = BUser
        fields = (
                'username',
                'email',
                'password1',
                'password2',
                )



class TaskForm(ModelForm):
    class Meta:
        model = BNotePost
        fields = (
                'title',
                'article',
                'user_post',
            )
