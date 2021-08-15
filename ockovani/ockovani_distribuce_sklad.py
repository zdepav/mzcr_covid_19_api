from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class OckovaniDistribuceSklad:
    """ Přehled distribuce očkovacích látek v ČR z centrálního skladu

    Datová sada obsahuje přehled distribuce očkovacích látek proti onemocnění COVID-19 v rámci
    centrálního skladu (příjem na centrální skladu a výdej do očkovacích míst v ČR). Každý záznam
    (řádek) datové sady udává počet ampulek dané očkovací látky, která byla daným očkovacím místem v
    daný den přijata nebo vydána.

    Attributes
    ----------

    datum: date
        Datum, kdy byla akce (distribuční záznam) uživatelem zadána do systému.

    akce: str
        Příznak, zda se jedná o příjem na sklad (objednané nebo již přijaté dodávky na centrálním
        skladě, příznak vždy neznamená, že se jedná o naskladněnou dodávku, může jít o dodávku
        objednanou) nebo výdej z centrálního skladu na poskytovatele zdravotních služeb (dle
        Národního registru poskytovatelů zdravotních služeb - NRPZS), případně je možné specifikovat
        přímo očkovací místo. Atribut nrpzs_kod a nrpzs_nazev jsou při výdeji povinné, atributy
        ockovaci_misto_id a ockovaci_misto_nazev jsou povinné pouze v případě, pokud je daný
        poskytovatel současně očkovacím místem.

    vyrobce: str
        Název výrobce distribuované očkovací látky.

    pocet_ampulek: int
        Počet ampulek, které byly součástí akce (distribučního záznamu), tedy příjem nebo výdej
        (Comirnaty (Pfizer) = 6 dávek / ampulka, VAXZEVRIA = 10 dávek / ampulka, Spikevax (Moderna)
        = 10 dávek / ampulka, COVID-19 Vaccine Janssen = 5 dávek / ampulka).

    nrpzs_kod: str
        Identifikátor poskytovatele zdravotních služeb dle registru NRPZS.

    nrpzs_nazev: str
        Název poskytovatele zdravotních služeb dle registru NRPZS.

    nrpzs_kraj_nazev: str
        Název kraje pro sídlo poskytovatele zdravotních služeb dle registru NRPZS.

    ockovaci_misto_id: str
        Jednoznačný identifikátor očkovacího místa.

    ockovaci_misto_nazev: str
        Název očkovacího místa.

    distribuce_id: str
        Identifikátor akce (distribučního záznamu), který umožňuje sprárování s datovou sadou o
        distribuci očkovacích látek mezi očkovacími místy.

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.akce: str = line[1]
        self.vyrobce: str = line[2]
        self.pocet_ampulek: int = int_field(line[3])
        self.nrpzs_kod: str = line[4]
        self.nrpzs_nazev: str = line[5]
        self.nrpzs_kraj_nazev: str = line[6]
        self.ockovaci_misto_id: str = line[7]
        self.ockovaci_misto_nazev: str = line[8]
        self.distribuce_id: str = line[9]


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['OckovaniDistribuceSklad'] :
        return get_many('ockovani-distribuce-sklad',
                        OckovaniDistribuceSklad,
                        ApiVersion.V2,
                        cache_dir)

