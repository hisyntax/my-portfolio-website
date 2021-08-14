from django import forms
from tinymce import TinyMCE
from .models import Article, Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Article
        # fields = ('title', 'overview', 'content', 'thumbnail', 
        # 'categories', 'featured', 'previous_post', 'next_post')
        fields = '__all__'

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'E.g This is my comment...', 'style': 'width: 100%; max-width: 70%; border:2px solid #5000ca; border-radius: 5px; padding:5px; outline: none; display: block; margin-bottom: 5px'
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'E.g JohnDoe@gmail.com...', 'style': 'width: 100%; max-width: 70%; border:2px solid #5000ca; border-radius: 5px; padding:5px; outline: none; display: block; margin-bottom: 5px'
    }))
    
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'John Doe...', 'style': 'width: 100%; max-width: 70%; border:2px solid #5000ca; border-radius: 5px; padding:5px; outline: none; display: block; margin-bottom: 5px'
    }))
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')