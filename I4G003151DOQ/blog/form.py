from django import forms
from .models import blog


# creating a form
class blogForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = blog

        # specify fields to be used
        fields = [
            "title",
            "description",
        ]