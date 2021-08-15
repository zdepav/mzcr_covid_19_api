from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class KrajOkresNakazeniVyleceniUmrti:
    """ Přehled epidemiologické situace dle hlášení krajských hygienických stanic podle okresu

    Datová sada podle krajů a okresů ČR obsahující kumulativní denní počty osob s prokázaným
    onemocněním COVID-19 dle validovaných hlášení krajských hygienických stanic, kumulativní denní
    počty vyléčených po onemocnění COVID-19 dle hlášení krajských hygienických stanic a kumulativní
    denní počty úmrtí v souvislosti s onemocněním COVID-19 dle hlášení krajských hygienických stanic
    a hospitalizačních úmrtí. S ohledem na fakt, že vykazování vyléčených osob a úmrtí má určité
    zpoždění oproti reálnému stavu z důvodu validace a uzavírání případů krajských hygienických
    stanic, se mohou denní záznamy zpětně výrazně měnit právě z důvodu průběžného doplňování.
    Nedoporučujeme uvádět aktuální počty aktivních případů na základě aktuálních počtů vyléčených
    osob a úmrtí za poslední dny. Data jsou neúplná a jejich použití má za následek zkreslující
    výsledky. V souladu s rozhodnutím sekce hlavní hygieničky Ministerstva zdravotnictví ČR budou na
    webu COVID-19 publikovány celkové počty aktivních případů COVID-19 až zpětně, a to po doplnění a
    po validaci dat s časovým odstupem 4 týdnů.

    Attributes
    ----------

    datum: date

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

    kumulativni_pocet_nakazenych: int
        Kumulativní počet osob s prokázanou nákazou.

    kumulativni_pocet_vylecenych: int
        Kumulativní počet vyléčených osob.

    kumulativni_pocet_umrti: int
        Kumulativní počet úmrtí.

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.kraj_nuts_kod: str = line[1]
        self.okres_lau_kod: str = line[2]
        self.kumulativni_pocet_nakazenych: int = int_field(line[3])
        self.kumulativni_pocet_vylecenych: int = int_field(line[4])
        self.kumulativni_pocet_umrti: int = int_field(line[5])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['KrajOkresNakazeniVyleceniUmrti'] :
        return get_many('kraj-okres-nakazeni-vyleceni-umrti',
                        KrajOkresNakazeniVyleceniUmrti,
                        ApiVersion.V2,
                        cache_dir)

