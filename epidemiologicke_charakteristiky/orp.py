from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class Orp:
    """ Přehled epidemiologické situace dle hlášení krajských hygienických stanic podle ORP

    Obsahem je komplexní přehled základních epidemiologických parametrů (počty diagnostikovaných
    osob s COVID-19, počty aktuálně nakažených, hospitalizovaní pacienti) se zaměřením na seniorní
    zranitelné skupiny obyvatel (kategorie věku 65+, 75+) na geografické úrovni obcí s rozšířenou
    působností (ORP).

    Attributes
    ----------

    den: str
        Označení příslušného dne.

    datum: date

    orp_kod: str
        Kód obce s rozšířenou působností dle číselníku ÚZIS ČR (https://pzu-api.uzis.cz/api/orp).

    orp_nazev: str
        Název obce s rozšířenou působností.

    incidence_7: int
        Celkový počet všech nově diagnostikovaných za týden zpětně ode dne uvedeného ve sloupci
        Datum.

    incidence_65_7: int
        Celkový počet nově diagnostikovaných ve věkové skupině 65+ za týden zpětně ode dne uvedeného
        ve sloupci Datum.

    incidence_75_7: int
        Celkový počet nově diagnostikovaných ve věkové skupině 75+ za týden zpětně ode dne uvedeného
        ve sloupci Datum.

    prevalence: int
        Aktuální počet aktivních případů ve stavu COVID+.

    prevalence_65: int
        Aktuální počet aktivních případů ve věkové skupině 65+ ve stavu COVID+.

    prevalence_75: int
        Aktuální počet aktivních případů ve věkové skupině 75+ ve stavu COVID+.

    aktualni_pocet_hospitalizovanych_osob: int
        Aktuální počet hospitalizovaných (dle bydliště v daném ORP).

    nove_hosp_7: int
        Celkový počet nově hospitalizovaných za týden zpětně ode dne uvedeného ve sloupci Datum (dle
        bydliště v daném ORP).

    testy_7: int
        Celkový počet provedených PCR testů za týden zpětně ode dne uvedeného ve sloupci Datum (dle
        bydliště v daném ORP).

    """

    def __init__(self, line: List[str]) :
        self.den: str = line[0]
        self.datum: Optional[date] = date_field(line[1])
        self.orp_kod: str = line[2]
        self.orp_nazev: str = line[3]
        self.incidence_7: int = int_field(line[4])
        self.incidence_65_7: int = int_field(line[5])
        self.incidence_75_7: int = int_field(line[6])
        self.prevalence: int = int_field(line[7])
        self.prevalence_65: int = int_field(line[8])
        self.prevalence_75: int = int_field(line[9])
        self.aktualni_pocet_hospitalizovanych_osob: int = int_field(line[10])
        self.nove_hosp_7: int = int_field(line[11])
        self.testy_7: int = int_field(line[12])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['Orp'] :
        return get_many('orp', Orp, ApiVersion.V2, cache_dir)

