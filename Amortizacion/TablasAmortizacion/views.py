from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import CalculoAmortizacion
from .utils import FilaAmortizacionIgual, amortizacionIgual

class Index(FormView):
    template_name = "Index.html"
    form_class = CalculoAmortizacion
    
    def form_valid(self, form):
        #Capturamos lo que necesitamos del post y lo casteamos
        periodosRango = int(self.request.POST['tiempo'])
        capitalInicial = float(self.request.POST['capitalInicial'])
        tasaInteres = float(self.request.POST['tasaInteres'])
        dias = float(self.request.POST['dias'])
        periodos = float(periodosRango)
        
        #Siempre las vamos a usar
        TE = tasaInteres*(dias/360)
        TE100 = TE/100
        
        #Creamos nuestra primera lista para amortizacionIgual
        lamortizacionIgual = amortizacionIgual(TE,TE100,periodosRango,periodos,capitalInicial)
        
        
            

        return render(
            self.request,
            self.template_name,
            {'solicitudes' : lamortizacionIgual, }
        )