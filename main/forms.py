from django import forms

class AddNewResources(forms.Form):
    name= forms.CharField(label="name", max_length=200)
    link= forms.CharField(label="urllink", max_length=200)
    remarks= forms.CharField(label="Remarks/Rating", max_length=200)
