from ..api import get_many, ApiVersion, int_field, bool_field
from typing import Iterator, List, Optional

class PrehledOckovacichMist:
    """ Očkovací místa v ČR

    Datová sada poskytuje seznam veřejných očkovacích míst v ČR, kde jsou podávány očkovací látky
    proti onemocnění COVID-19.

    Attributes
    ----------

    ockovaci_misto_id: str
        Jednoznačný identifikátor očkovacího místa.

    ockovaci_misto_nazev: str
        Název očkovacího místa.

    okres_nuts_kod: str
         Identifikátor okresu podle klasifikace NUTS4, kde se očkovací místo nachází.

    operacni_status: bool
        Příznak, zda je očkovací místo veřejné. V datové sadě jsou uveřejněna pouze veřejná očkovací
        místa.

    ockovaci_misto_adresa: str
        Adresa očkovacího místa.

    latitude: str
        Souřadnice (zeměpisná šířka) určující polohu očkovacího místa.

    longitude: str
        Souřadnice (zeměpisná délka) určující polohu očkovacího místa.

    ockovaci_misto_typ: str
        Typ očkovacího místa (OČM: očkovací místo, VOČM: velkokapacitní očkovací místo, DOČM:
        distribuční očkovací místo)

    nrpzs_kod: int
        Kód zdravotnického zařízení podle Národního registru poskytovatelů zdravotních služeb. Jedno
        zdravotnické zařízení může disponovat jedním nebo více očkovacími místy.

    minimalni_kapacita: int
        Minimalní kapacita očkovaných osob za jeden den.

    bezbarierovy_pristup: bool
        Příznak, zda očkovací místo disponuje bezbarierovým přístupem.

    """

    def __init__(self, line: List[str]) :
        self.ockovaci_misto_id: str = line[0]
        self.ockovaci_misto_nazev: str = line[1]
        self.okres_nuts_kod: str = line[2]
        self.operacni_status: bool = bool_field(line[3])
        self.ockovaci_misto_adresa: str = line[4]
        self.latitude: str = line[5]
        self.longitude: str = line[6]
        self.ockovaci_misto_typ: str = line[7]
        self.nrpzs_kod: int = int_field(line[8])
        self.minimalni_kapacita: int = int_field(line[9])
        self.bezbarierovy_pristup: bool = bool_field(line[10])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['PrehledOckovacichMist'] :
        return get_many('prehled-ockovacich-mist', PrehledOckovacichMist, ApiVersion.V2, cache_dir)

