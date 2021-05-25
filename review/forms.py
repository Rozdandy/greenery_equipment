from django import forms
from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    """
    Create a form for users to add reviews
    """
    class Meta:
        model = ProductReview
        exclude = (
            'user',
            'date_added',
            'product',
            'likes',
            'unlikes')

        fields = ['topic', 'body', 'rate']

        labels = {
            'rate': 'Rate',
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders for the review form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'topic': 'Topic',
            'body': 'Body',
        }

        # Add placeholders and classes to input fields
        self.fields['topic'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rate':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False

            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
