from django import forms

class NewBlogPostForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class newCommentForm(forms.Form):
    author = forms.CharField()
    title = forms.CharField()
    text = forms.CharField()