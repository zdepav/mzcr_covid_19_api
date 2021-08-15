from ..api import get_many, ApiVersion, int_field, float_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class Incidence_7_14_Kraje:
    """ Přehled osob s prokázanou nákazou dle krajských hygienických stanic včetně laboratoří za 7 a
    14 dní podle krajů

    Datová sada obsahující počty potvrzených případů za posledních 7 a 14 dní za kraje ČR včetně
    přepočtu na 100 000 obyvatel. Pro přepočet na 100 000 obyvatel je použita otevřená datová sada
    Obyvatelstvo podle pětiletých věkových skupin a pohlaví v krajích a okresech
    (https://www.czso.cz/csu/czso/obyvatelstvo-podle-petiletych-vekovych-skupin-a-pohlavi-v-krajich-a-okresech).

    Attributes
    ----------

    datum: date

    kraj_nuts_kod: str
        Identifikátor kraje podle klasifikace NUTS 3, ve kterém byly případy diagnostikovány.

    kraj_nazev: str
        Název kraje, ve kterém byly případy diagnostikovány.

    incidence_7: int
        Celkový počet nově diagnostikovaných případů za předchozích 7 dní ode dne uvedeného ve
        sloupci "datum".

    incidence_14: int
        Celkový počet nově diagnostikovaných případů za předchozích 14 dní ode dne uvedeného ve
        sloupci "datum".

    incidence_7_100000: float
        Celkový počet nově diagnostikovaných případů za předchozích 7 dní ode dne uvedeného ve
        sloupci "datum", který je přepočtený na 100 000 obyvatel.

    incidence_14_100000: float
        Celkový počet nově diagnostikovaných případů za předchozích 14 dní ode dne uvedeného ve
        sloupci "datum", který je přepočtený na 100 000 obyvatel.

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.kraj_nuts_kod: str = line[1]
        self.kraj_nazev: str = line[2]
        self.incidence_7: int = int_field(line[3])
        self.incidence_14: int = int_field(line[4])
        self.incidence_7_100000: float = float_field(line[5])
        self.incidence_14_100000: float = float_field(line[6])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['Incidence_7_14_Kraje'] :
        return get_many('incidence-7-14-kraje', Incidence_7_14_Kraje, ApiVersion.V2, cache_dir)

