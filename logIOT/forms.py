from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, ButtonHolder
from crispy_forms.bootstrap import Accordion, AccordionGroup, Tab
from .models import Device, Channel

# New device form class based upon Django model form
class DeviceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # Call base calss constructor
        super(DeviceForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance,
        # it builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_id = 'registrationForm'
        self.helper.form_class = 'site_form form-horizontal'
        self.helper.label_class = 'col-xs-2 col-md-2'
        self.helper.field_class = 'col-xs-10 col-md-10'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset('Device Details',
                'name',
                'description',
                'image'),
            Fieldset('Device Location',
                'latitude',
                'longitude'),
            Fieldset(' ',
                'public'),
            Div(
                Submit('submit', 'Save Device', css_class='btn btn-default'),
                css_class='col-xs-offset-2 col-md-offset-2')
        )

        #self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        # Database model type (we are adding a Device)
        model = Device
        # Fields for model (same as in user models file)
        fields = ['name', 'description', 'image', 'latitude', 'longitude', 'public']
        # Add/override data for models fields
        labels = {
            'image': _('Image URL'),
            'public': _('Make public?'),
        }


class ChannelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # Call base calss constructor
        super(ChannelForm, self).__init__(*args, **kwargs)
        # If you pass FormHelper constructor a form instance,
        # it builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_id = 'channelForm'
        self.helper.form_class = 'site_form form-horizontal'
        self.helper.label_class = 'col-xs-2 col-md-2'
        self.helper.field_class = 'col-xs-10 col-md-10'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset('Channel Details',
                'name'),
            Fieldset('Sensor Details',
                'sensor_type',
                'units'),
            Div(
                Submit('submit', 'Save Channel', css_class='btn btn-default'),
                css_class='col-xs-offset-2 col-md-offset-2')
        )

        #self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        # Database model type (we are adding a Device)
        model = Channel
        # Fields for model (same as in user models file)
        fields = ['name', 'sensor_type', 'units']
        # Add/override data for models fields
        labels = {
            'sensor_type': _('sensor type'),
        }
