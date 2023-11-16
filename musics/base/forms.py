from django import forms

from musics.base.models import User


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['full_name', 'username', 'password']
