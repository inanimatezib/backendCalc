from django import forms

from calc.models import Formula


class FormulaForm(forms.ModelForm):
    class Meta:
        model = Formula
        fields = ["x1", "x2", "x3"]

