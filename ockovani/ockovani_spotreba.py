from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class OckovaniSpotreba:
    """ Přehled spotřeby podle očkovacích míst ČR

    Datová sada obsahuje přehled spotřeby očkovacích látek (použité a znehodnocené ampulky) proti
    onemocnění COVID-19 v očkovacích místech v ČR. Každý záznam (řádek) datové sady udává počet
    použitých a znehodnocených ampulek dané očkovací látky na daném očkovacím místě v daný den.

    Attributes
    ----------

    datum: date
        Den, kdy byly spotřebovány ampulky dané očkovací látky

    ockovaci_misto_id: str
        Jednoznačný identifikátor očkovacího místa.

    ockovaci_misto_nazev: str
        Název očkovacího místa

    kraj_nuts_kod: str
        Identifikátor kraje podle klasifikace NUTS 3, ve kterém se nachází očkovací místo.

    kraj_nazev: str
        Název kraje podle klasifikace NUTS 3, ve kterém se nachází očkovací místo.

    ockovaci_latka: str
        Název spotřebované očkovací látky.

    vyrobce: str
        Název výrobce spotřebované očkovací látky.

    pouzite_ampulky: int
        Počet ampulek očkovací látky, které byly použity.

    znehodnocene_ampulky: int
        Počet ampulek očkovací látky, které byly znehodnoceny.

    pouzite_davky: int
        Počet použitých dávek očkovací látky (přepočet dávek v jedné ampulce podle informací
        výrobce): Comirnaty (Pfizer) = 6 dávek/ampulka, COVID-19 Vaccine AstraZeneca (AstraZeneca) =
        10 dávek/ampulka, Spikevax (Moderna) = 10 dávek/ampulka.

    znehodnocene_davky: int
        Počet znehodnocených dávek očkovací látky (přepočet dávek v jedné ampulce podle informací
        výrobce): Comirnaty (Pfizer) = 6 dávek/ampulka, COVID-19 Vaccine AstraZeneca (AstraZeneca) =
        10 dávek/ampulka, Spikevax (Moderna) = 10 dávek/ampulka.

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.ockovaci_misto_id: str = line[1]
        self.ockovaci_misto_nazev: str = line[2]
        self.kraj_nuts_kod: str = line[3]
        self.kraj_nazev: str = line[4]
        self.ockovaci_latka: str = line[5]
        self.vyrobce: str = line[6]
        self.pouzite_ampulky: int = int_field(line[7])
        self.znehodnocene_ampulky: int = int_field(line[8])
        self.pouzite_davky: int = int_field(line[9])
        self.znehodnocene_davky: int = int_field(line[10])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['OckovaniSpotreba'] :
        return get_many('ockovani-spotreba', OckovaniSpotreba, ApiVersion.V2, cache_dir)

