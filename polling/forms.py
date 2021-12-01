from django.forms import ModelForm
from polling.models import Poll


class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ["title", "text"]
