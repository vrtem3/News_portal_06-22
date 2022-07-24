from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)  # Задаем минимальную длину текста публикации при создании новой публикации через форму

    class Meta:
        model = Post
        fields = '__all__'
       
    def clean(self):
        cleaned_data = super().clean()
        post_title = cleaned_data.get("post_title")
        text = cleaned_data.get("text")

        if post_title == text:
            raise ValidationError(
                "Текст публикации не должен быть идентичен названию."
            )

        return cleaned_data

