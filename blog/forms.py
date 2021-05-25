from .models import Post, Comment, Image
from django import forms
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
	class Meta:
	    model = Post
	    fields = ('title', 'content', 'image')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
       
