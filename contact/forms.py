from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from contact.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )    
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'style': 'resize: vertical; min-height: 39px; max-height: 200px;',
                'rows': 4,
            }
        )
    )
    
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',)
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
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField(
        required=True
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('A user with that email already exists.', code='invalid'),
            )
        return email