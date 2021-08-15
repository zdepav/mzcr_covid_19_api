from ..api import get_many, ApiVersion, int_field, bool_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class Osoby :
    """ Přehled osob s prokázanou nákazou dle hlášení krajských hygienických stanic (v2)

    Datová sada obsahující základní denní incidenční přehled osob s prokázanou nákazou COVID-19 dle
    hlášení krajských hygienických stanic (datum hlášení, věk a pohlaví nakažené osoby, KHS,
    informace o místě a zemi nákazy). Datová sada nahrazuje předchozí verzi dostupnou na adrese
    https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/ .

    Attributes
    ----------

    datum: date

    vek: int

    pohlavi: str

    kraj_nuts_kod: str
        Identifikátor kraje podle klasifikace NUTS 3, ve kterém byla pozitivní nákaza hlášena
        krajskou hygienickou stanicí. V případě, že není uvedena žádná hodnota, nebylo možné
        identifikovat místo bydliště nakažené osoby. Jde o problém se ztotožňováním bydliště v
        reálném čase u minority případů, kdy není uvedeno bydliště ze šetření KHS a jsou dostupná
        pouze data z laboratoří. Bydliště je správně určeno na úrovni kraje a okresu, ale došlo k
        chybnému přiřazení osob ke konkrétní obci.

    okres_lau_kod: str
        Identifikátor okresu podle klasifikace LAU 1. V případě, že není uvedena žádná hodnota,
        nebylo možné identifikovat místo bydliště nakažené osoby. Jde o problém se ztotožňováním
        bydliště v reálném čase u minority případů, kdy není uvedeno bydliště ze šetření KHS a jsou
        dostupná pouze data z laboratoří. Bydliště je správně určeno na úrovni kraje a okresu, ale
        došlo k chybnému přiřazení osob ke konkrétní obci.

    nakaza_v_zahranici: bool
        Příznak, zda došlo k nákaze mimo ČR.

    nakaza_zeme_csu_kod: str
        Identifikátor státu v zahraničí, kde došlo k nákaze (dvoumístný kód z číselníku zemí CZEM).

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.vek: int = int_field(line[1])
        self.pohlavi: str = line[2]
        self.kraj_nuts_kod: str = line[3]
        self.okres_lau_kod: str = line[4]
        self.nakaza_v_zahranici: bool = bool_field(line[5])
        self.nakaza_zeme_csu_kod: str = line[6]


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['Osoby'] :
        return get_many('osoby', Osoby, ApiVersion.V2, cache_dir)

