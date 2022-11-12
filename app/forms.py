from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from app.models import Theme


class ThemeForm(forms.ModelForm):
    title = forms.CharField(max_length=123,
                            label='Title',
                            validators=(
                                MinLengthValidator(limit_value=2, message=''),
                                )
                            )

    class Meta:
        model = Theme
        fields = ('title', 'author', 'description')

    def clean_tite(self):
        title = self.cleaned_data('description')
        if Theme.objects.filter(description=title).exists():
            raise ValidationError('Such themes exist')
        return title


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Find')
