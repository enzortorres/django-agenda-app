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
        label='First name',
        help_text='Type your first name.',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # self.fields['first_name'].widget.attrs.update({
        #     'placeholder': 'First Name'
        # })
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category')
        # widgets = {
        #     'first_name': forms.TextInput(
        #             attrs={
        #                 'placeholder': 'First Name',
        #             }
        #         ),
        # }
    
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError(
                    'Primeiro nome não pode ser igual ao segundo'
                )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não pode colocar ABC nesse campo',
                    code='invalid'
                )
            )
        
        return first_name