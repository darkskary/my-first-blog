from django import forms
from .models import Post, Comentario

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = 'text',


class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('coment' ,'fk_post')
        widgets = {'fk_post': forms.HiddenInput()}
