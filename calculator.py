def validates_float(number: float) -> bool:
    if isinstance(number, float):
        return True
    raise ValueError(f"Valor {number} não é numérico.")


def addition(numero1: float, numero2: float) -> float:
    if validates_float(numero1) and validates_float(numero2):
        return numero1 + numero2


def subtaction(numero1: float, numero2: float) -> float:
    if validates_float(numero1) and validates_float(numero2):
        return numero1 - numero2


def multiplication(numero1: float, numero2: float) -> float:
    if validates_float(numero1) and validates_float(numero2):
        return numero1 * numero2


def division(numero1: float, numero2: float) -> float:
    try:
        if validates_float(numero1) and validates_float(numero2):
            return numero1 / numero2
    except ZeroDivisionError as erro:
        raise erro




