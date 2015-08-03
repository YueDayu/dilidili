from django import forms
from .models import Video

class VideoUploadForm(forms.ModelForm):
	class Meta:
		model = Video
		fields = ['name', 'describe', 'video', 'image', 'tag', 'category_set']
		widgets = {
			'category_set': forms.CheckboxSelectMultiple
		}
