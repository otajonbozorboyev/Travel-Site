from django import forms

from apps.pages.models import TourCategory


class TourCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = TourCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.status:  # Agar status False bo'lsa
            self.fields.pop('city', None)  # 'city' maydonini olib tashlash
            self.fields.pop('place', None)  # 'place' maydonini olib tashlash
