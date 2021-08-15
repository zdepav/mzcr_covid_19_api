from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class OckovaniDistribuce:
    """ Přehled distribuce očkovacích látek v ČR

    Datová sada obsahuje přehled distribuce očkovacích látek proti onemocnění COVID-19 do očkovacích
    míst v ČR. Každý záznam (řádek) datové sady udává počet ampulek dané očkovací látky, která byla
    daným očkovacím místem v daný den přijata nebo vydána.

    Attributes
    ----------

    datum: date
        Den, kdy byla provedena distribuce na dané očkovací místo.

    ockovaci_misto_id: str
        Jednoznačný identifikátor očkovacího místa.

    ockovaci_misto_nazev: str
        Název očkovacího místa.

    kraj_nuts_kod: str
        Identifikátor kraje podle klasifikace NUTS 3, ve kterém se nachází očkovací místo.

    kraj_nazev: str
        Název kraje podle klasifikace NUTS 3, ve kterém se nachází očkovací místo.

    cilove_ockovaci_misto_id: str
        Kód cílového očkovacího místa, kam je očkovací látka distribuována.

    cilove_ockovaci_misto_nazev: str
        Název cílového očkovacího místa, kam je očkovací látka distribuována.

    cilovy_kraj_kod: str
        Identifikátor kraje podle klasifikace NUTS 3, ve kterém se nachází očkovací místo, kam je
        očkovací látka distribuována.

    cilovy_kraj_nazev: str
        Název kraje podle klasifikace NUTS 3, ve kterém se nachází očkovací místo, kam je očkovací
        látka distribuována.

    ockovaci_latka: str
        Název distribuované očkovací látky.

    vyrobce: str
        Název výrobce distribuované očkovací látky.

    akce: str
        Příznak, zda se jedná v rámci distribučního procesu o příjem nebo výdej očkovací látky.
        Příznak „příjem“ označuje, že daná očkovací látka byla dodána na dané očkovací místo z
        centrálního skladu (cílové očkovací místo není vyplněno). Příznak „výdej“ označuje, že daná
        očkovací látka byla dále distribuována očkovacím místem na cílové očkovací místo (cílové
        očkovací místo je vyplněno, v případě nevyplnění cílové očkovací místo není evidováno v
        centrálním systému – např. praktický lékař).

    pocet_ampulek: int
        Počet ampulek distribuované očkovací látky. Počty dávek očkovací látky podle výrobce:
        Comirnaty (Pfizer) = 6 dávek/ampulka, COVID-19 Vaccine AstraZeneca (AstraZeneca) = 10
        dávek/ampulka, Spikevax (Moderna) = 10 dávek/ampulka, COVID-19 Vaccine Janssen (Janssen) =
        10 dávek/ampulka.

    pocet_davek: int
        Počet dávek distribuované očkovací látky (přepočet dávek v jedné ampulce podle informací
        výrobce): Comirnaty (Pfizer) = 6 dávek/ampulka, COVID-19 Vaccine AstraZeneca (AstraZeneca) =
        10 dávek/ampulka, Spikevax (Moderna) = 10 dávek/ampulka, COVID-19 Vaccine Janssen (Janssen)
        = 10 dávek/ampulka.

    distribuce_id: str
        Identifikátor distribučního záznamu, který umožňuje sprárovat příjmy a výdaje očkovacíh
        látek s datovou sadou o distribuci z centrálního skladu.

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.ockovaci_misto_id: str = line[1]
        self.ockovaci_misto_nazev: str = line[2]
        self.kraj_nuts_kod: str = line[3]
        self.kraj_nazev: str = line[4]
        self.cilove_ockovaci_misto_id: str = line[5]
        self.cilove_ockovaci_misto_nazev: str = line[6]
        self.cilovy_kraj_kod: str = line[7]
        self.cilovy_kraj_nazev: str = line[8]
        self.ockovaci_latka: str = line[9]
        self.vyrobce: str = line[10]
        self.akce: str = line[11]
        self.pocet_ampulek: int = int_field(line[12])
        self.pocet_davek: int = int_field(line[13])
        self.distribuce_id: str = line[14]


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['OckovaniDistribuce'] :
        return get_many('ockovani-distribuce', OckovaniDistribuce, ApiVersion.V2, cache_dir)

