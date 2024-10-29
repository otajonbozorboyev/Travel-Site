from django import forms
from .models import BookingTour, Subscription


class PackageForm(forms.ModelForm):
    class Meta:
        model = BookingTour
        fields = ["full_name", "email", "data_time", 'destination', 'persons', 'kids', 'message']

    def __init__(self, *args, **kwargs):
        super(PackageForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control p-3'
            field.widget.attrs['placeholder'] = field_name.title()


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control border-primary rounded-pill w-100 py-3 ps-4 pe-5'
            field.widget.attrs['placeholder'] = field_name.title()