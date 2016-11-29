from django import forms

class CalculoAmortizacion(forms.Form):
    meses = (('3','3 Meses'),
             ('6','6 Meses'),
             ('12','12 Meses'),
             ('24','24 Meses'),
             ('36','36 Meses'),
             ('48','48 Meses'),
             ('60','60 Meses'),
             ('72','72 Meses'))
    tiempo = forms.ChoiceField(choices=meses)
    capitalInicial = forms.FloatField(label='Capital Inicial', 
                                        widget=forms.TextInput(attrs={'placeholder': '40000'}))
    tasaInteres = forms.FloatField(label = 'Tasa Interes', 
                                     widget=forms.TextInput(attrs={'placeholder': '12'}))
    dias = forms.IntegerField(label = 'Dias', 
                                     widget=forms.TextInput(attrs={'placeholder': '60'}))
    
    