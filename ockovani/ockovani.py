from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class Ockovani:
    """ Přehled vykázaných očkování podle krajů ČR

    Datová sada poskytuje agregovaná data o vykázaných očkováních na úrovni krajů ČR. Každý řádek
    přehledu popisuje počet vykázaných očkování v daném dni, za věkovou skupinu, s použitím vybrané
    očkovací látky a ve vybraném kraji. Za jeden den tedy přehled obsahuje maximálně X řádků, kde
    X = počet krajů (14) x počet věkových skupin (15) x počet druhů očkovacích látek (v okamžik
    publikace 4) = 840. Data jsou aktualizována k času 20.00 h předchozího dne a mohou se zpětně
    mírně měnit z důvodu průběžného doplňování.

    Attributes
    ----------

    datum: date
        Datum, ve kterém byla očkování v daném kraji provedena.

    vakcina: str
        Název očkovací látky.

    kraj_nuts_kod: str
        Identifikátor kraje podle klasifikace NUTS 3, ve kterém se nachází očkovací místo.

    kraj_nazev: str
        Název kraje, ve kterém se nachází očkovací místo.

    vekova_skupina: str
        Rozdělení očkovaných osob podle věku do skupin: 0-17, 18-24, 25-29, 30-34, 35-39, 40-44,
        45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75-79, 80+, nezařazeno - pokud nelze určit věkovou
        skupinu.

    prvnich_davek: int
        Počet osob, které v daném kraji a v daném dni obdrželi první dávku dané očkovací látky.

    druhych_davek: int
        Počet osob, které v daném kraji a v daném dni obdrželi druhou dávku dané očkovací látky.

    celkem_davek: int
        Celkový počet osob, které v daném kraji a v daném dni obdrželi dávku dané očkovací látky
        (součet prvních a druhých dávek dané očkovací látky).

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.vakcina: str = line[1]
        self.kraj_nuts_kod: str = line[2]
        self.kraj_nazev: str = line[3]
        self.vekova_skupina: str = line[4]
        self.prvnich_davek: int = int_field(line[5])
        self.druhych_davek: int = int_field(line[6])
        self.celkem_davek: int = int_field(line[7])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['Ockovani'] :
        return get_many('ockovani', Ockovani, ApiVersion.V2, cache_dir)

