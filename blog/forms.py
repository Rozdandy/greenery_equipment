from django import forms
from .models import Comment
from .models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'article']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['article'].label = "Comment"
