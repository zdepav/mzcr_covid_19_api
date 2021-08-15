from ..api import get_many, ApiVersion, int_field, bool_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class OckovaciZarizeni:
    """ Očkovací zařízení

    Datová sada poskytuje seznam očkovacích zařízení v ČR jako doplnění seznamu očkovacích míst, kde
    jsou podávány očkovací látky proti onemocnění COVID-19. Jedná se především o praktické lékaře,
    ale i další, kde se očkování provádí.

    Attributes
    ----------

    zarizeni_kod: str
        Kód zdravotnického zařízení, ve kterém je prováděno očkování (podle číselníku poskytovatelů
        zdravotních služeb na úrovni jednotlivých zařízení).

    zarizeni_nazev: str
        Název zdravotnického zařízení, ve kterém je prováděno očkování.

    provoz_zahajen: bool
        Příznak, zda bylo zahájeno očkování v daném zdravotnickém zařízení.

    kraj_nuts_kod: str
        Identifikátor kraje podle klasifikace NUTS 3, ve kterém se nachází očkovací místo.

    kraj_nazev: str
        Název kraje, ve kterém se nachází očkovací místo.

    okres_lau_kod: str
        Identifikátor okresu podle klasifikace LAU 1, ve kterém se očkovací zařízení nachází.

    okres_nazev: str
        Název okresu, ve kterém se očkovací zařízení nachází.

    zrizovatel_kod: int
        Kód zřizovatele zdravotnického zařízení podle číselníku ÚZIS.

    zrizovatel_nazev: str
        Název zřizovatele zdravotnického zařízení.

    provoz_ukoncen: date
        Datum, kdy bylo ukončeno očkování v daném zdravotnickém zařízení.

    prakticky_lekar: bool
        Příznak, zda se jedná o praktického lékaře.

    """

    def __init__(self, line: List[str]) :
        self.zarizeni_kod: str = line[0]
        self.zarizeni_nazev: str = line[1]
        self.provoz_zahajen: bool = bool_field(line[2])
        self.kraj_nuts_kod: str = line[3]
        self.kraj_nazev: str = line[4]
        self.okres_lau_kod: str = line[5]
        self.okres_nazev: str = line[6]
        self.zrizovatel_kod: int = int_field(line[7])
        self.zrizovatel_nazev: str = line[8]
        self.provoz_ukoncen: Optional[date] = date_field(line[9])
        self.prakticky_lekar: bool = bool_field(line[10])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['OckovaciZarizeni'] :
        return get_many('ockovaci-zarizeni', OckovaciZarizeni, ApiVersion.V2, cache_dir)

