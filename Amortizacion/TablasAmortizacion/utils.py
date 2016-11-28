class FilaAmortizacionIgual:
    def __init__(self, periodo, capitalInicial, amortizacion,interes,pago,capitalFinal):
        self.periodo = periodo
        self.capitalInicial = capitalInicial
        self.amortizacion = amortizacion
        self.interes = interes
        self.pago = pago
        self.capitalFinal = capitalFinal

def amortizacionIgual(TE,TE100,periodosRango,periodos,capitalInicial):
    lista = []
    amortizacionFija = round(capitalInicial/periodos,2)
    capitalInicial2 = 0;
    for i in range(0,periodosRango):
        interes = round(TE100*capitalInicial,2)
        pago = round(amortizacionFija + interes,2)

        if(i == periodosRango-2):
            capitalFinal = amortizacionFija
        else:
            capitalFinal = capitalInicial-amortizacionFija
        s = FilaAmortizacionIgual(1+i,capitalInicial,amortizacionFija,interes,pago,capitalFinal)
        capitalInicial = capitalFinal
        lista.append(s)
    return lista