from django import forms
from shops import models


class Category_create(forms.Form):
    title = forms.CharField(max_length=200)


class Product_create(forms.Form):
    img = forms.ImageField(required=False)
    title = forms.CharField(max_length=24)
    description = forms.CharField(widget=forms.Textarea)
    rate = forms.FloatField()
    category = forms.ModelChoiceField(queryset=models.Category.objects.all())
    prize = forms.FloatField()
    phone_number = forms.FloatField()

class CommentsCreateForm(forms.Form):
    text = forms.CharField(max_length=355)

