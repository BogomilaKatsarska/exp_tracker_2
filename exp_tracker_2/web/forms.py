import os

from django import forms

from exp_tracker_2.web.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ('budget', 'first_name', 'last_name', 'profile_image')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'profile_image')


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.profile_image.path
        if commit:
            self.instance.delete()
            os.remove(image_path)
            return self.instance

    class Meta:
        model = Profile
        fields = ()
