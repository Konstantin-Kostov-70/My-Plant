from django import forms

from My_exam.my_plant.models import Plant


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
