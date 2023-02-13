from django.core.exceptions import ValidationError
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'category_type',
            'postCategory',
            'title',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        if text is not None and len(text) < 20:
            raise ValidationError({
                'text': 'Текст новости не может быть менее 20 символов'
            })

        title = cleaned_data.get('title')
        if title == text:
            raise ValidationError(
                'Текст новости не должен быть идентичен названию новости'
            )
        if title[0].islower():
            raise ValidationError(
                'Название новости должно начинаться с заглавной буквы'
            )
        return cleaned_data


