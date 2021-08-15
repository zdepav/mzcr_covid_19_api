from ..api import get_many, ApiVersion, int_field, bool_field
from typing import Iterator, List, Optional

class PrehledOdberovychMist:
    """ Odběrová místa v ČR

    Datová sada poskytuje seznam odběrových míst v ČR, kde jsou prováděny PCR a antigenní testy na
    onemocnění COVID-19. Součástí publikovaného seznamu nejsou odběrová místa ve zdravotnických
    zařízeních, kde jsou prováděny testy před přijetím pacienta v souvislosti s poskytováním
    neodkladné péče. Mobilní odběrové týmy mají kapacitu pevně nastavenu (na hodnotu 20), protože
    není možné přesně určit tuto kapacitu.

    Attributes
    ----------

    odberove_misto_id: str
        Jednoznačný identifikátor odběrového místa.

    odberove_misto_nazev: str
        Název odběrového místa.

    okres_nuts_kod: str
         Identifikátor okresu podle klasifikace NUTS4, kde se očkovací místo nachází.

    operacni_status: bool
        Příznak, zda je oodběrové místo v provozu (https://registrace.mzcr.cz/).

    odberove_misto_adresa: str
        Adresa odběrového místa.

    latitude: str
        Souřadnice (zeměpisná šířka) určující polohu odběrového místa.

    longitude: str
        Souřadnice (zeměpisná délka) určující polohu odběrového místa.

    testovaci_kapacita: int
        Celkový počet vzorků nezávisle na typu odběru (nasofaryngeální, orofaryngeální nebo
        antigenní odběr), které je schopno odběrové místo provést za den.

    nasofaryngealni_odber: bool
        Příznak, zda odběrové místo provádí PCR testy nasofaryngeálně.

    orofaryngealni_odber: bool
        Příznak, zda odběrové místo provádí PCR testy orofaryngeálně.

    antigenni_odber: bool
        Příznak, zda odběrové místo provádí antigenní testy.

    drive_in: bool
        Příznak, zda odběrové místo funguje v tzv. drive-in režimu (pacienti přijíždějí autem a
        nevystupují).

    """

    def __init__(self, line: List[str]) :
        self.odberove_misto_id: str = line[0]
        self.odberove_misto_nazev: str = line[1]
        self.okres_nuts_kod: str = line[2]
        self.operacni_status: bool = bool_field(line[3])
        self.odberove_misto_adresa: str = line[4]
        self.latitude: str = line[5]
        self.longitude: str = line[6]
        self.testovaci_kapacita: int = int_field(line[7])
        self.nasofaryngealni_odber: bool = bool_field(line[8])
        self.orofaryngealni_odber: bool = bool_field(line[9])
        self.antigenni_odber: bool = bool_field(line[10])
        self.drive_in: bool = bool_field(line[11])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['PrehledOdberovychMist'] :
        return get_many('prehled-odberovych-mist', PrehledOdberovychMist, ApiVersion.V2, cache_dir)

