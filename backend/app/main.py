"""
Este módulo define la API principal del Simulador de Préstamos,
incluyendo configuraciones de FastAPI, rutas y validaciones.
"""

from datetime import datetime  # Importación estándar
from dateutil.relativedelta import relativedelta  # Importación de terceros

# Importaciones de terceros agrupadas
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Agrupada con fastapi
from pydantic import BaseModel  # Importación de terceros

# Importaciones locales
from app.utils.calculos import calcular_amortizacion_francesa, calcular_pago_carencia
from app.routes.prestamos import router as prestamos_router  # Importaciones locales

# Instancia de FastAPI con metadatos
app = FastAPI(
    title="Simulador de Préstamos",
    description="API para simular préstamos con cálculo de cuotas mensuales, pagos durante periodos de carencia y fecha de finalización.",
    version="1.0.0",
    contact={
        "name": "Soporte del Simulador",
        "email": "soporte@simulador.com",
    },
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    # Permitir todos los orígenes (restringir en producción)
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Incluir rutas desde prestamos.py
app.include_router(
    prestamos_router, prefix="/api/prestamos", tags=["Préstamos"]
)

# Modelos de datos


class PrestamoRequest(BaseModel):
    capital: float
    tasa_interes: float
    duracion_meses: int
    periodo_carencia: bool = False
    meses_carencia: int = 0
    fecha_inicio: str  # Formato: DD/MM/AAAA


class PrestamoResponse(BaseModel):
    cuota_mensual: float
    pagos_carencia: list[float] = []
    fecha_finalizacion: str

# Ruta principal para simular préstamo


@app.post("/simular", response_model=PrestamoResponse, tags=["Simulaciones"])
def simular_prestamo(request: PrestamoRequest):
    """
    Simula un préstamo con cuota mensual, periodo de carencia opcional
    y fecha estimada de finalización.
    """

    # Validar fecha de inicio
    try:
        fecha_inicio = datetime.strptime(request.fecha_inicio, "%d/%m/%Y")
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail="Formato de fecha inválido. Use DD/MM/AAAA.",
        ) from exc

    # Validaciones adicionales
    if request.duracion_meses <= 0:
        raise HTTPException(
            status_code=400,
            detail="La duración del préstamo debe ser mayor a 0 meses.",
        )
    if request.capital <= 0:
        raise HTTPException(
            status_code=400,
            detail="El capital debe ser mayor a 0.",
        )
    if request.tasa_interes <= 0:
        raise HTTPException(
            status_code=400,
            detail="La tasa de interés debe ser mayor a 0.",
        )
    if request.periodo_carencia and request.meses_carencia < 0:
        raise HTTPException(
            status_code=400,
            detail="El número de meses de carencia no puede ser negativo.",
        )

    # Cálculo de la cuota mensual
    cuota_mensual = calcular_amortizacion_francesa(
        request.capital, request.tasa_interes, request.duracion_meses
    )

    # Cálculo del periodo de carencia
    pagos_carencia = (
        calcular_pago_carencia(
            request.capital, request.tasa_interes, request.meses_carencia)
        if request.periodo_carencia
        else []
    )

    # Fecha de finalización del préstamo
    fecha_finalizacion = fecha_inicio + \
        relativedelta(months=request.duracion_meses)

    # Retornar respuesta
    return PrestamoResponse(
        cuota_mensual=cuota_mensual,
        pagos_carencia=pagos_carencia,
        fecha_finalizacion=fecha_finalizacion.strftime("%d/%m/%Y"),
    )

# Ruta de prueba para verificar el estado del servidor


@app.get("/", tags=["Root"])
def read_root():
    """
    Ruta de prueba para verificar que el servidor está activo.
    """
    return {
        "message": "¡Bienvenido al Simulador de Préstamos!",
        "documentation": "/docs",
    }
