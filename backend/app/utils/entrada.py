from colorama import Fore, Style


def entrada_datos(mensaje, tipo=float):
    """
    Solicita entrada de datos al usuario y valida el tipo de dato.
    - mensaje: Texto que se mostrará al usuario.
    - tipo: Tipo de dato que se espera (por defecto, float).
    """
    while True:
        try:
            return tipo(input(mensaje))
        except ValueError:
            print(
                f"{Fore.RED}Entrada inválida. Por favor, introduce un {tipo.__name__}.{Style.RESET_ALL}")


def entrada_opcion(opciones, mensaje):
    """
    Solicita al usuario una opción válida de una lista.
    - opciones: Lista de opciones válidas.
    - mensaje: Texto que se mostrará al usuario.
    """
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones:
            return opcion
        print(
            f"{Fore.RED}Opción no válida. Selecciona entre {', '.join(opciones)}.{Style.RESET_ALL}")
