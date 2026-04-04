from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _

from .models import Aircraft, AircraftPhoto


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class AircraftAdminForm(forms.ModelForm):
    class Meta:
        model = Aircraft
        fields = (
            "type",
            "model",
            "tail_number",
            "tail_color",
            "register_number",
            "serial_number",
            "subdivision",
            "status",
            "date",
            "location",
            "description",
        )

    photos = MultipleImageField(
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        files = self.files.getlist("photos")
        for upload in files:
            validate_image_file_extension(upload)
        return files

    def save_photos(self, aircraft):
        for upload in self.files.getlist("photos"):
            photo = AircraftPhoto(aircraft=aircraft, image=upload)
            photo.save()