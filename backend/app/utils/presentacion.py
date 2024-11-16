from colorama import Fore, Style
from constantes import SEPARADOR_TITULO, SEPARADOR_SECCION


def imprimir_titulo(texto):
    """Imprime un título destacado."""
    print(f"\n{Fore.CYAN}{SEPARADOR_TITULO}")
    print(f"{Fore.CYAN}{texto.center(50)}")
    print(f"{Fore.CYAN}{SEPARADOR_TITULO}{Style.RESET_ALL}")


def imprimir_seccion(texto):
    """Imprime un subtítulo para secciones."""
    print(f"\n{Fore.GREEN}{SEPARADOR_SECCION}")
    print(f"{Fore.GREEN}{texto.center(50)}")
    print(f"{Fore.GREEN}{SEPARADOR_SECCION}{Style.RESET_ALL}")


def imprimir_tabla_intereses(pagos):
    """Imprime una tabla de los intereses pagados mes a mes."""
    print(f"\n{Fore.LIGHTMAGENTA_EX}{'Mes':<10}{'Intereses (EUR)':>20}")
    print(f"{'-' * 30}{Style.RESET_ALL}")
    for mes, interes in enumerate(pagos, start=1):
        print(f"{mes:<10}{interes:>20.2f}")


def imprimir_resumen(capital_pendiente, cuota_mensual, fecha_finalizacion):
    """Muestra un resumen final de la simulación."""
    print(f"\n{Fore.YELLOW}{SEPARADOR_TITULO}")
    print(f"{'RESUMEN DE TU PRÉSTAMO'.center(50)}")
    print(f"{SEPARADOR_TITULO}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Capital pendiente: {capital_pendiente:.2f} EUR")
    print(f"Cuota mensual: {cuota_mensual:.2f} EUR")
    print(
        f"Fecha de finalización estimada: {fecha_finalizacion.strftime('%d/%m/%Y')}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{SEPARADOR_TITULO}{Style.RESET_ALL}")
