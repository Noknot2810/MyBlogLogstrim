from django import forms

class CreateForm(forms.Form):
    article_title = forms.CharField(label="New article title", max_length=100)
    article_text = forms.CharField(label="New article title", max_length=500)
