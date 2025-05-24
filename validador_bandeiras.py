def validar_mastercard(numero):
    if len(numero) == 16 and numero.startswith(("51", "52", "53", "54", "55")):
        return True
    return False


def validar_visa(numero):
    if len(numero) == 16 and numero.startswith("4"):
        return True
    return False


def validar_amex(numero):
    if len(numero) == 15 and numero.startswith(("34", "37")):
        return True
    return False


def validar_diners_club(numero):
    if len(numero) == 14 and numero.startswith(("36", "38", "39")):
        return True
    return False


def validar_discover(numero):
    if len(numero) == 16 and numero.startswith(
        ("6011", "644", "645", "646", "647", "648", "649", "65")
    ):
        return True
    return False


def validar_enroute(numero):
    if len(numero) in [15, 16] and numero.startswith("201") or numero.startswith("214"):
        return True
    return False


def validar_jcb(numero):
    if len(numero) in [16, 15] and numero.startswith(("3528", "3589")):
        return True
    return False


def validar_voyager(numero):
    if len(numero) == 15 and numero.startswith("869"):
        return True
    return False


def validar_hipercard(numero):
    if len(numero) in [13, 16] and numero.startswith(("606282", "3841", "637", "60")):
        return True
    return False


def validar_aura(numero):
    if len(numero) in [13, 15, 16] and numero.startswith(
        ("50", "51", "52", "53", "54", "55")
    ):
        return True
    return False


def validar_cartao(numero):
    numero = numero.replace(" ", "").replace("-", "")
    if validar_mastercard(numero):
        return "MasterCard"
    elif validar_visa(numero):
        return "Visa"
    elif validar_amex(numero):
        return "American Express"
    elif validar_diners_club(numero):
        return "Diners Club"
    elif validar_discover(numero):
        return "Discover"
    elif validar_enroute(numero):
        return "enRoute"
    elif validar_jcb(numero):
        return "JCB"
    elif validar_voyager(numero):
        return "Voyager"
    elif validar_hipercard(numero):
        return "HiperCard"
    elif validar_aura(numero):
        return "Aura"
    else:
        return "Bandeira não reconhecida"
