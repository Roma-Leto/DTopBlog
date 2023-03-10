from django.forms import ModelForm
from .models import BNotePost
from django.contrib.auth.decorators import login_required

class TaskForm(ModelForm):
    class Meta:
        model = BNotePost
        fields = (
                'title',
                'article',
                'user_post',
            )
