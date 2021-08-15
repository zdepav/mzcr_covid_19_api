from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class NakazeniVyleceniUmrtiTesty:
    """ Celkový (kumulativní) počet osob s prokázanou nákazou dle krajských hygienických stanic
    včetně laboratoří, počet vyléčených, počet úmrtí a provedených testů (v2)

    Datová sada obsahující kumulativní denní počty osob s prokázaným onemocněním COVID-19 dle
    hlášení krajských hygienických stanic včetně laboratoří, denní počty vyléčených po onemocnění
    COVID‑19 dle hlášení krajských hygienických stanic, denní počty úmrtí v souvislosti s
    onemocněním COVID‑19 dle hlášení krajských hygienických stanic a hospitalizačních úmrtí, a denní
    počty provedených testů na onemocnění COVID-19 dle hlášení laboratoří. S ohledem na fakt, že
    vykazování vyléčených osob a úmrtí má určité zpoždění oproti reálnému stavu z důvodu validace a
    uzavírání případů krajských hygienických stanic, se mohou denní záznamy zpětně měnit právě z
    důvodu průběžného doplňování. Datová sada nahrazuje předchozí verzi dostupnou na adrese
    https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/ .

    Attributes
    ----------

    datum: date

    kumulativni_pocet_nakazenych: int
        Kumulativní počet osob s prokázanou nákazou.

    kumulativni_pocet_vylecenych: int
        Kumulativní počet vyléčených osob.

    kumulativni_pocet_umrti: int
        Kumulativní počet úmrtí.

    kumulativni_pocet_testu: int
        Kumulativní počet provedených PCR testů.

    kumulativni_pocet_ag_testu: int
        Kumulativní počet provedených antigenních testů.

    prirustkovy_pocet_nakazenych: int
        Přírůstkový počet osob s prokázanou nákazou.

    prirustkovy_pocet_vylecenych: int
        Přírůstkový počet vyléčených osob.

    prirustkovy_pocet_umrti: int
        Přírůstkový počet úmrtí.

    prirustkovy_pocet_provedenych_testu: int
        Přírůstkový počet provedených PCR testů.

    prirustkovy_pocet_provedenych_ag_testu: int
        Přírůstkový počet provedených antigenních testů.

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.kumulativni_pocet_nakazenych: int = int_field(line[1])
        self.kumulativni_pocet_vylecenych: int = int_field(line[2])
        self.kumulativni_pocet_umrti: int = int_field(line[3])
        self.kumulativni_pocet_testu: int = int_field(line[4])
        self.kumulativni_pocet_ag_testu: int = int_field(line[5])
        self.prirustkovy_pocet_nakazenych: int = int_field(line[6])
        self.prirustkovy_pocet_vylecenych: int = int_field(line[7])
        self.prirustkovy_pocet_umrti: int = int_field(line[8])
        self.prirustkovy_pocet_provedenych_testu: int = int_field(line[9])
        self.prirustkovy_pocet_provedenych_ag_testu: int = int_field(line[10])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['NakazeniVyleceniUmrtiTesty'] :
        return get_many('nakazeni-vyleceni-umrti-testy',
                        NakazeniVyleceniUmrtiTesty,
                        ApiVersion.V2,
                        cache_dir)

