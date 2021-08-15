from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class OckovaciMista:
    """ Přehled vykázaných očkování podle očkovacích míst ČR

    Datová sada poskytuje řádková data o vykázaných očkováních na jednotlivých očkovacích místech
    ČR. Každý řádek přehledu popisuje jedno vykázané očkování v daném dni a věkové skupině, s
    použitím vybrané očkovací látky, na konkrétním očkovacím místu a ve vybraném kraji.

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

    zarizeni_kod: str
        Kód zdravotnického zařízení, ve kterém se nachází očkovací místo (podle číselníku
        poskytovatelů zdravotních služeb na úrovni jednotlivých zařízení).

    zarizeni_nazev: str
        Název zdravotnického zařízení, ve kterém se nachází očkovací místo.

    poradi_davky: int
        Pořadí dávky (první, druhá) danou očkovací látkou.

    vekova_skupina: str
        Rozdělení očkovaných osob podle věku do skupin: 0-17, 18-24, 25-29, 30-34, 35-39, 40-44,
        45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75-79, 80+, nezařazeno - pokud nelze určit věkovou
        skupinu.

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.vakcina: str = line[1]
        self.kraj_nuts_kod: str = line[2]
        self.kraj_nazev: str = line[3]
        self.zarizeni_kod: str = line[4]
        self.zarizeni_nazev: str = line[5]
        self.poradi_davky: int = int_field(line[6])
        self.vekova_skupina: str = line[7]


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['OckovaciMista'] :
        return get_many('ockovaci-mista', OckovaciMista, ApiVersion.V2, cache_dir)

