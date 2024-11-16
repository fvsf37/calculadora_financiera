from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from dateutil.relativedelta import relativedelta
from app.utils.calculos import calcular_amortizacion_francesa, calcular_pago_carencia
from app.routes.prestamos import router as prestamos_router

# Instancia de FastAPI
app = FastAPI(title="Simulador de Préstamos")

# Incluir rutas desde prestamos.py
app.include_router(
    prestamos_router, prefix="/api/prestamos", tags=["Préstamos"])

# Modelo de solicitud


class PrestamoRequest(BaseModel):
    capital: float
    tasa_interes: float
    duracion_meses: int
    periodo_carencia: bool = False
    meses_carencia: int = 0
    fecha_inicio: str  # En formato "DD/MM/AAAA"

# Modelo de respuesta


class PrestamoResponse(BaseModel):
    cuota_mensual: float
    pagos_carencia: list[float] = []
    fecha_finalizacion: str


@app.post("/simular", response_model=PrestamoResponse)
def simular_prestamo(request: PrestamoRequest):
    # Validar fecha de inicio
    try:
        fecha_inicio = datetime.strptime(request.fecha_inicio, "%d/%m/%Y")
    except ValueError:
        raise HTTPException(
            status_code=400, detail="Formato de fecha inválido. Use DD/MM/AAAA.")

    # Cálculo de la cuota mensual
    cuota_mensual = calcular_amortizacion_francesa(
        request.capital, request.tasa_interes, request.duracion_meses
    )

    # Cálculo del periodo de carencia
    pagos_carencia = []
    if request.periodo_carencia:
        pagos_carencia = calcular_pago_carencia(
            request.capital, request.tasa_interes, request.meses_carencia
        )

    # Fecha de finalización del préstamo
    fecha_finalizacion = fecha_inicio + \
        relativedelta(months=request.duracion_meses)

    # Respuesta
    return PrestamoResponse(
        cuota_mensual=cuota_mensual,
        pagos_carencia=pagos_carencia,
        fecha_finalizacion=fecha_finalizacion.strftime("%d/%m/%Y")
    )
