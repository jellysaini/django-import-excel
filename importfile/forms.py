from django import forms
from django.core.exceptions import ValidationError
import openpyxl
from io import BytesIO
import pandas as pd


class FarmerImport(forms.Form):
    file = forms.FileField(required=False)

    def send_file(self):
        file = self.cleaned_data['file']

        df =  pd.read_excel(file.read())
        return df.to_html()
