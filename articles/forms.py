from email.policy import default
from django import forms
from matplotlib.image import thumbnail
from . import models
from ckeditor.widgets import CKEditorWidget


class CreateArticleForm(forms.ModelForm):
    body = forms.CharField(widget = CKEditorWidget())
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug','thumbnail']

class EditArticleForm(forms.ModelForm):
    def __init__(self, title, body, thumbnail,*args, **kwargs):
        super(EditArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].initial = title
        self.fields['body'].initial = body
    
    body = forms.CharField(widget = CKEditorWidget())
    class Meta:
        model = models.Article
        fields = ['title', 'body']
    
class SubmittedArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body']
        widgets = {
            'body': CKEditorWidget(),
        }

    # def clean_slug(self):
    #     new_slug = self.cleaned_data['slug'].lower()

    #     if new_slug == 'create':
    #         raise forms.ValidationError('Slug may not be "create"')
    #     if models.Article.objects.filter(slug__iexact=new_slug).count():
    #         raise forms.ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
    #     return new_slug