from django import  forms

from .models import Contact

class ContactForm(forms.ModelForm):

    comment=forms.CharField(max_length=500,label=("comment"),widget=forms.Textarea(attrs={'rows':"2"}))

    class Meta:
        model=Contact
        fields=[
        'name',
        'email',
        'comment',
        ]
