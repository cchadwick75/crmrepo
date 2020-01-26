'''forms.py - written by Collin Chadwick'''
# pylint: disable=too-few-public-methods
from django import forms
from django.forms import ModelForm
from administration.models import Customer

class CreateCustomerForm(ModelForm):
    '''
    New Create Customer Form that is based off of the Customer Model.
    The attributes are changed to fit the bootstrap layout and visual standard
    '''

    class Meta(object):
        '''
        This will perform the attributes setting for the customer model to be functional with HTML
        '''
        def __init__(self):
            pass
        model = Customer


        fields = ['name', 'phone', 'street_address', 'street_address2', 'city', 'state', 'zip_code']



        widgets = {'name': forms.TextInput(attrs={'class':'form-control',
                                                       'id':'name',
                                                       'required': True,
                                                       'placeholder': 'Enter Customer Name',
                                                       'autocomplete': 'off'

                                                      }),

                   'phone': forms.TextInput(attrs={'class': 'form-control',
                                                   'id': 'id_phone',
                                                   'required': False,
                                                   'placeholder': 'Enter Numbers Only, Formatting Is Automatic',
                                                   'label': 'Phone Number',
                                                   'autocomplete': 'off',
                                                   }),

                   'street_address': forms.TextInput(attrs={'class': 'form-control',
                                                            'id': 'id_street_address',
                                                            'required': True,
                                                            'placeholder': 'Enter Address 1',
                                                            'label': 'Address 1',
                                                            'autocomplete': 'off'
                                                            }),

                   'street_address2': forms.TextInput(attrs={'class': 'form-control',
                                                             'id': 'id_street_address2',
                                                             'required': False,
                                                             'placeholder': 'Enter Address 2',
                                                             'label': 'Address 2',
                                                             'autocomplete': 'off'
                                                             }),

                   'city': forms.TextInput(attrs={'class': 'form-control',
                                                  'id': 'id_city',
                                                  'required': False,
                                                  'placeholder': 'City',
                                                  'label': 'City',
                                                  'autocomplete': 'off',
                                                  }),

                   'state': forms.Select(attrs={'class': 'form-control',
                                                'id': 'id_state',
                                                'required': True,
                                                'placeholder': 'Choose State',
                                                'label': 'State',
                                                'autocomplete': 'off',
                                                }),

                   'zip_code': forms.TextInput(attrs={'class': 'form-control',
                                                      'id': 'id_zip_code',
                                                      'required': False,
                                                      'placeholder': 'Zip Code',
                                                      'label': 'Zip Code',
                                                      'autocomplete': 'off',
                                                      })


                  }
