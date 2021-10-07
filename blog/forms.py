from django import forms
from .models import Comment,NewsLetter,Contact
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author','body']


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']

class SearchForm(forms.Form):
    query = forms.CharField()

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message']

class TagForm(forms.Form):
    name = forms.CharField()
