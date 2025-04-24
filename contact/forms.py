from django.core.exceptions import ValidationError
from contact.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
            } 
        ),
        label='Primeiro nome',
        help_text='Digite o seu primeiro nome',
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # self.fields['first_name'].widget.attrs.update({
        #     'placeholder': 'First Name'
        # })
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)
        # widgets = {
        #     'first_name': forms.TextInput(
        #             attrs={
        #                 'placeholder': 'First Name',
        #             }
        #         ),
        # }
    
    def clean(self):
        cleaned_data = self.cleaned_data
        
        self.add_error(
            'fist_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
        self.add_error(
            'last_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        
        return super().clean()