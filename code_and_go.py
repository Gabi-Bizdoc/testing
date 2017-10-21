
def nume_de_functie(de_exemplu, chestii_de_genu="lol"):
    print(str(de_exemplu).upper(),
          str(chestii_de_genu).lower())


def alta_functie(ceva_argument, ceva_lista=None,
                 alt_argument=None,
                 *args, **kwargs):
    """Prints arguments and appends 1st arg to 2nd."""
    # ceva_lista = ceva_lista or []
    # if ceva_lista == None:
    if not ceva_lista:
        ceva_lista = []

    if 'nu_stiu' in kwargs:
        print("<<<BINGOO!! Cum te cheama? "
              "%s>>>" % kwargs['nu_stiu'])

    ceva_lista.append(ceva_argument)
    print(ceva_argument, ceva_lista, args, kwargs)


"""
nume_de_functie("ceva", "ALTCEVA")
nume_de_functie("ceVA", "altCEVA")
nume_de_functie("ceva", 1)
nume_de_functie("ceva", None)

nume_de_functie('cica')
"""

lista = ['element']
alta_functie('arg', [])
alta_functie('alt arg', lista)
alta_functie('inca un arg', lista)

alta_functie('gigi')
alta_functie("petrolieru'")

alta_functie('muncitoru\'', alt_argument=[1, 2])

alta_functie("petrolieru'", [], 'blabla', 'blabescu',
             'blibli', 'bloobloo', nu_stiu="ma")

"""
def alta_functie(ceva_argument, ceva_lista=None,
                 alt_argument=None,
                 *args, **kwargs):
"""

# alta_functie(ceva_argument='inca_ceva', [1, 2, 3])
print(help(alta_functie))


def suma_si_produs(a, b):
    return a + b, a * b


za_suma, za_produs = suma_si_produs(3, 2)
print(za_suma, za_produs)


def operatii(a, b):
    print("Yielding a + b")
    yield a + b

    print("Yielding a - b")
    yield a - b

    print("Yielding a * b")
    yield a * b

    print("Yielding a ** b")
    yield a ** b


for rezultat in operatii(10, 4):
    print(rezultat)
    if rezultat < 10:
        break


def functiune(argument_dubios):
    if (argument_dubios is None or
            'dubios' in argument_dubios):
        raise Exception(
            "Ba, argumentul ala e dubios! %s" % argument_dubios)

    print("ceva")


try:
    functiune(None)
    functiune(-1)
    functiune('Ce dubiosenie!')
except TypeError as exc:
    print("lol, ti-e belit codul.")
except Exception as exc:
    print(exc)

functiune("ceva perfect normal.")


class MyException(Exception):
    message = "Ceva mai specific."
