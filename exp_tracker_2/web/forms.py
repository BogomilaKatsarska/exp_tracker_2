from django import forms

from exp_tracker_2.web.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ('budget', 'first_name', 'last_name', 'profile_image')
        