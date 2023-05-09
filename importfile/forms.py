from django import forms
from django.core.validators import FileExtensionValidator
from pathlib import Path
from io import BytesIO
import pandas as pd


class FarmerImport(forms.Form):
    file = forms.FileField(required=False,validators=[FileExtensionValidator(['csv','xls','xlsx'])])

    def send_file(self):
        file = self.cleaned_data['file']
        extension = Path(file.name).suffix[1:].lower()
        if extension == 'csv':
            df = pd.read_csv(BytesIO(file.read()))
        else:
            # assuming file is excel
            df =  pd.read_excel(file.read())
        return df.to_html()
