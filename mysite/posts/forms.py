from django import forms


from .models import Post


class PostForm(forms.ModelForm):
    
    title       = forms.CharField(label='title',
                    widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    content = forms.CharField(widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "Your content",
                                        "rows": 10,
                                        'cols': 30
                                    }
                                ))
    # update = forms.DateField()
    # create_date = forms.DateField()
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            # 'update',
            # 'create_date'
        ]
