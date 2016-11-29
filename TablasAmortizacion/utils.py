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

def tipoBullet(TE,TE100,periodosRango,periodos,capitalInicial):
    lista = []
    amortizacionFija = round(capitalInicial,2)
    interes = round(TE100*capitalInicial,2)
    pago = interes
    capitalFinal = capitalInicial
    for i in range(0,periodosRango):
        if(i == periodosRango-1):
            amortizacionFija = capitalInicial
            pago = amortizacionFija+interes
            capitalFinal = 0.0
        else:
            amortizacionFija = 0.0
        s = FilaAmortizacionIgual(1+i,capitalInicial,amortizacionFija,interes,pago,capitalFinal)
        lista.append(s)
    return lista

def crecientes(TE,TE100,periodosRango,periodos,capitalInicial):
    lista = []
    capitalInicial2 = capitalInicial
    for i in range(0,periodosRango):
        interes = round(capitalInicial*TE100,2)
        i2 = float(1+i)
        pago = round((capitalInicial2/periodos)*(1+TE100)**i2,2)
        amortizacionFija = pago - interes
        if(i == periodosRango-1):
            capitalFinal = 0.0
        else:
            capitalFinal = capitalInicial - amortizacionFija
        
        s = FilaAmortizacionIgual(1+i,capitalInicial,amortizacionFija,interes,pago,capitalFinal)
        capitalInicial = capitalFinal
        lista.append(s)
    return lista

def iguales(TE,TE100,periodosRango,periodos,capitalInicial):
    lista = []
    capitalInicial2 = capitalInicial
    for i in range(0,periodosRango):
        interes = round(capitalInicial*TE100,2)
        pago = round(capitalInicial2*(TE100/(1-(1+TE100)**(-periodos))),2)
        amortizacionFija = pago - interes
        if(i == periodosRango-1):
            capitalFinal = 0.0
            amortizacionFija = capitalInicial
        else:
            capitalFinal = capitalInicial - amortizacionFija
        s = FilaAmortizacionIgual(1+i,capitalInicial,amortizacionFija,interes,pago,capitalFinal)
        capitalInicial = capitalFinal
        lista.append(s)
    return lista