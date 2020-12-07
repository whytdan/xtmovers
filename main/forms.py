from django import forms
from .models import ApplicationModel

class ApplicationForm(forms.ModelForm):
    is_moved_up = forms.ChoiceField( 
                 choices=ApplicationModel.ANSWERS,
                 widget=forms.RadioSelect(attrs={'class' : 'Radio'}), initial='Y')
    
    next_is_moved_up = forms.ChoiceField( 
                 choices=ApplicationModel.ANSWERS,
                 widget=forms.RadioSelect(attrs={'class' : 'Radio'}), initial='Y')

    extra_items = forms.ChoiceField( 
                 choices=ApplicationModel.ANSWERS,
                 widget=forms.RadioSelect(attrs={'class' : 'Radio'}), initial='Y')
    
    phone_number = forms.CharField(min_length=17)
    
    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs={
            'placeholder': 'First Name...'
        }
        self.fields['last_name'].widget.attrs={
            'placeholder': 'Last Name...'
        }
        self.fields['phone_number'].widget.attrs={
            'placeholder': 'Phone number...'
        }
        self.fields['email'].widget.attrs={
            'placeholder': 'Email...'
        }
        self.fields['moving_from'].widget.attrs={
            'placeholder': 'Apartment, house, townhouse, etc...',
            'list': 'moving_from_list'
        }
        self.fields['house_size'].widget.attrs={
            'placeholder': 'Studio, 1 bd, 2 bd, 3 bd, 4bd, etc...',
            'list': 'house_size_list'
        }
        self.fields['address'].widget.attrs={
            'placeholder': 'Address...',
        }
        self.fields['moving_into'].widget.attrs={
            'placeholder': 'Apartment, house, townhouse, etc...',
            'list': 'moving_to_list'
        }
        self.fields['next_house_size'].widget.attrs={
            'placeholder': 'Studio, 1 bd, 2 bd, 3 bd, 4bd, etc...',
            'list': 'next_house_size_list'
        }
        self.fields['next_address'].widget.attrs={
            'placeholder': 'Address...',
        }
        self.fields['additional_service'].widget.attrs={
            'placeholder': 'Additional service...',
            'spellcheck': 'false'
        }
        self.fields['comments'].widget.attrs={
            'placeholder': 'I would like to...',
            'spellcheck': 'false'
        }

    class Meta:
        model = ApplicationModel
        fields = '__all__'


