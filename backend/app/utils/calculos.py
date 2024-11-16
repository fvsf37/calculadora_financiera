from datetime import datetime
from dateutil.relativedelta import relativedelta


def calcular_amortizacion_francesa(capital, tasa_interes, meses):
    """
    Calcula la cuota mensual según el sistema de amortización francesa.
    - capital: Monto del préstamo.
    - tasa_interes: Tasa de interés anual en porcentaje.
    - meses: Duración del préstamo en meses.
    """
    tasa_mensual = tasa_interes / 12 / 100
    return capital * tasa_mensual / (1 - (1 + tasa_mensual) ** -meses)


def calcular_pago_carencia(capital, tasa_interes, meses_carencia):
    """
    Calcula los pagos de intereses durante el periodo de carencia.
    - capital: Monto del préstamo.
    - tasa_interes: Tasa de interés anual en porcentaje.
    - meses_carencia: Número de meses en el periodo de carencia.
    """
    pagos = []
    for _ in range(meses_carencia):
        intereses = capital * (tasa_interes / 12 / 100)
        pagos.append(intereses)
    return pagos
