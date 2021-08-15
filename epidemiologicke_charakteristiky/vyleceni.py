from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class Vyleceni :
    """ Přehled vyléčených dle hlášení krajských hygienických stanic

    Datová sada obsahující záznamy o vyléčených po onemocnění COVID‑19 dle hlášení krajských
    hygienických stanic. S ohledem na fakt, že vykazování vyléčených osob má určité zpoždění oproti
    reálnému stavu z důvodu validace a uzavírání případů krajských hygienických stanic, se mohou
    denní záznamy zpětně měnit právě z důvodu průběžného doplňování. Tento přehled je aktualizován
    vždy jednou týdně ve středu a obsahuje data k předchozí neděli.

    Attributes
    ----------

    datum: date

    vek: int

    pohlavi: str

    kraj_nuts_kod: str
        Identifikátor kraje podle klasifikace NUTS 3. V případě, že není uvedena žádná hodnota,
        nebylo možné identifikovat místo bydliště nakažené osoby. Jde o problém se ztotožňováním
        bydliště v reálném čase u minority případů, kdy není uvedeno bydliště ze šetření KHS a jsou
        dostupná pouze data z laboratoří. Bydliště je správně určeno na úrovni kraje a okresu, ale
        došlo k chybnému přiřazení osob ke konkrétní obci.

    okres_lau_kod: str
        Identifikátor okresu podle klasifikace LAU 1. V případě, že není uvedena žádná hodnota,
        nebylo možné identifikovat místo bydliště nakažené osoby. Jde o problém se ztotožňováním
        bydliště v reálném čase u minority případů, kdy není uvedeno bydliště ze šetření KHS a jsou
        dostupná pouze data z laboratoří. Bydliště je správně určeno na úrovni kraje a okresu, ale
        došlo k chybnému přiřazení osob ke konkrétní obci.

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.vek: int = int_field(line[1])
        self.pohlavi: str = line[2]
        self.kraj_nuts_kod: str = line[3]
        self.okres_lau_kod: str = line[4]


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['Vyleceni'] :
        return get_many('vyleceni', Vyleceni, ApiVersion.V2, cache_dir)

