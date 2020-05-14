from django import forms
from . import models
class Create_batches(forms.ModelForm):
    class Meta:
        model=models.batches
        fields=['batch_name','starting_year','ending_year','department','college','description','thumb']
class upload_excel(forms.ModelForm):
    class Meta:
        model=models.excel_raw_data
        fields=['excel_data']    
