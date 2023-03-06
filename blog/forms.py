from django.forms import ModelForm
from .models import BNotePost


class TaskForm(ModelForm):
    class Meta:
        model = BNotePost
        fields = [
                'title',
                'article',
            ]

