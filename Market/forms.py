from django.forms import ModelForm
from .models import Products
from django import forms


class PrForm(ModelForm):
    cost = forms.FloatField(label='цена', )
    outdate = forms.IntegerField(label='Проср.', initial=0)
    outdate = forms.IntegerField(label='Проср.', initial=0)
    count = forms.IntegerField(label='Кол.', initial=0)

    class Meta:
        model = Products
        fields = ('name', 'count', 'cost', 'outdate', 'categ')


class PrInitForm(ModelForm):
    ids = forms.IntegerField(label='')
    ids.widget.attrs['readonly'] = True
    cost = forms.FloatField(label='')
    name = forms.CharField(label='')
    outdate = forms.IntegerField(label='Проср.', initial=0)
    count = forms.IntegerField(label='Кол.', initial=0)

    class Meta:
        model = Products
        fields = ('ids', 'name', 'count', 'outdate', 'cost',)
