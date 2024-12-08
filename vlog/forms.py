from django import forms
from .models import VlogPost

class VlogPostForm(forms.ModelForm):
    class Meta:
        model = VlogPost
        fields = ['title', 'video_url', 'description', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.youtube.com/watch?v=VIDEO_ID'
            }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'tags': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter tags separated by spaces'
            }),
        }

    def clean_video_url(self):
        """Additional validation for video URL if needed"""
        url = self.cleaned_data.get('video_url')
        return url
