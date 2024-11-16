from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from dateutil.relativedelta import relativedelta
from app.utils.calculos import calcular_amortizacion_francesa, calcular_pago_carencia

# Crear un router
router = APIRouter()

# Modelo de entrada


class PrestamoRequest(BaseModel):
    capital: float
    tasa_interes: float
    duracion_meses: int
    periodo_carencia: bool = False
    meses_carencia: int = 0
    fecha_inicio: str  # Formato: DD/MM/AAAA

# Modelo de respuesta


class PrestamoResponse(BaseModel):
    cuota_mensual: float
    pagos_carencia: list[float] = []
    fecha_finalizacion: str


@router.post("/simular", response_model=PrestamoResponse)
def simular_prestamo(request: PrestamoRequest):
    """
    Simula un préstamo calculando la cuota mensual, pagos durante el periodo de carencia (si aplica),
    y la fecha estimada de finalización.
    """
    try:
        # Validar la fecha de inicio
        fecha_inicio = datetime.strptime(request.fecha_inicio, "%d/%m/%Y")
    except ValueError:
        raise HTTPException(
            status_code=400, detail="Formato de fecha inválido. Use DD/MM/AAAA."
        )

    # Validar que los valores numéricos sean positivos
    if request.capital <= 0:
        raise HTTPException(
            status_code=400, detail="El capital debe ser mayor que cero."
        )
    if request.tasa_interes <= 0:
        raise HTTPException(
            status_code=400, detail="La tasa de interés debe ser mayor que cero."
        )
    if request.duracion_meses <= 0:
        raise HTTPException(
            status_code=400, detail="La duración del préstamo debe ser mayor que cero."
        )
    if request.periodo_carencia and request.meses_carencia < 0:
        raise HTTPException(
            status_code=400,
            detail="La duración del periodo de carencia no puede ser negativa.",
        )

    # Calcular la cuota mensual
    cuota_mensual = calcular_amortizacion_francesa(
        request.capital, request.tasa_interes, request.duracion_meses
    )

    # Calcular pagos del periodo de carencia
    pagos_carencia = []
    if request.periodo_carencia:
        pagos_carencia = calcular_pago_carencia(
            request.capital, request.tasa_interes, request.meses_carencia
        )

    # Calcular la fecha de finalización
    fecha_finalizacion = fecha_inicio + \
        relativedelta(months=request.duracion_meses)

    # Retornar la respuesta
    return PrestamoResponse(
        cuota_mensual=cuota_mensual,
        pagos_carencia=pagos_carencia,
        fecha_finalizacion=fecha_finalizacion.strftime("%d/%m/%Y"),
    )
