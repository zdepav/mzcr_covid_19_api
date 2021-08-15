from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class TestyPcrAntigenni:
    """ Přehled provedených testů podle typu a indikace

    Datová sada obsahující denní počty provedených testů s rozlišením na PCR testy a antigenní testy
    na onemocnění COVID-19 dle hlášení laboratoří. Dále jsou v sadě uvedeny počty testů dle indikace
    (diagnostické indikace, epidemiologické indikace, preventivní a plošné testování, ostatní),
    pozitivní záchyty dle indikace testu a pozitivní záchyty dle typu testu (symptomy jsou
    objektivně vyšetřeny u indikovaných osob, v rámci plošného testování jde o vyjádření
    subjektivního posouzení testovaného). Zdrojem dat je centrální Informační systém infekčních
    nemocí (ISIN). Primární data byla analyticky zpracována a následně transformována do podoby
    publikovatelné online týmem ÚZIS ČR.

    Attributes
    ----------

    datum: date

    pocet_PCR_testy: int
        Přírůstkový počet provedených PCR testů.

    pocet_AG_testy: int
        Přírůstkový počet provedených antigenních testů.

    typologie_test_indik_diagnosticka: int
        Diagnostické indikace.

    typologie_test_indik_epidemiologicka: int
        Epidemiologické indikace.

    typologie_test_indik_preventivni: int
        Preventivní a plošné testování.

    typologie_test_indik_ostatni: int
        Ostatní.

    incidence_pozitivni: int
        Pozitivní záchyty dle indikace testu celkem.

    pozit_typologie_test_indik_diagnosticka: int
        Pozitivní záchyty dle indikace testu: diagnostické indikace.

    pozit_typologie_test_indik_epidemiologicka: int
        Pozitivní záchyty dle indikace testu: epidemiologické indikace.

    pozit_typologie_test_indik_preventivni: int
        Pozitivní záchyty dle indikace testu: preventivní a plošné testy.

    pozit_typologie_test_indik_ostatni: int
        Pozitivní záchyty dle indikace testu: ostatní.

    PCR_pozit_sympt: int
        Pozitivní záchyty dle PCR testu: symptomatické případy.

    PCR_pozit_asymp: int
        Pozitivní záchyty dle PCR testu: asymptomatické případy.

    AG_pozit_symp: int
        Pozitivní záchyty dle antigenního testu: PCR: symptomatické případy.

    AG_pozit_asymp_PCR_conf: int
        Pozitivní záchyty dle antigenního testu: asymptomatické případy (konfirmováno PCR).

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.pocet_PCR_testy: int = int_field(line[1])
        self.pocet_AG_testy: int = int_field(line[2])
        self.typologie_test_indik_diagnosticka: int = int_field(line[3])
        self.typologie_test_indik_epidemiologicka: int = int_field(line[4])
        self.typologie_test_indik_preventivni: int = int_field(line[5])
        self.typologie_test_indik_ostatni: int = int_field(line[6])
        self.incidence_pozitivni: int = int_field(line[7])
        self.pozit_typologie_test_indik_diagnosticka: int = int_field(line[8])
        self.pozit_typologie_test_indik_epidemiologicka: int = int_field(line[9])
        self.pozit_typologie_test_indik_preventivni: int = int_field(line[10])
        self.pozit_typologie_test_indik_ostatni: int = int_field(line[11])
        self.PCR_pozit_sympt: int = int_field(line[12])
        self.PCR_pozit_asymp: int = int_field(line[13])
        self.AG_pozit_symp: int = int_field(line[14])
        self.AG_pozit_asymp_PCR_conf: int = int_field(line[15])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['TestyPcrAntigenni'] :
        return get_many('testy-pcr-antigenni', TestyPcrAntigenni, ApiVersion.V2, cache_dir)

