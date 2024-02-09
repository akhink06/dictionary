from django import forms
from words.models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word', 'definition','synonymns']

        error_message = {
            "word" : {
                "required" : "word field is required"
            },
            "definition" : {
                "required" : "definition field is required"
            },
            "word" : {
                "synonymns" : "synonymns field is required"
            },
        }