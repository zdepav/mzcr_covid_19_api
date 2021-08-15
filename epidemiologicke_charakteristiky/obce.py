from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class Obce:
    """ Epidemiologická charakteristika obcí

    Obsah datové sady zahrnuje základní epidemiologické parametry (počty nově diagnostikovaných osob
    s COVID-19, počty aktuálně nakažených) na úrovni obcí ČR.

    Na základě informací z některých malých obcí eviduje správce systému ISIN problémy s přiřazením
    bydliště obyvatel. Jde o chybu ztotožňování bydliště v reálném čase u minority případů, kdy není
    uvedeno bydliště z šetření KHS a jsou dostupná pouze data z laboratoří. Bydliště je správně
    určeno na úrovni kraje a okresu, ale došlo k chybnému přiřazení osob ke konkrétní obci. Případy
    podle všeho patří do velkých měst, a drobné obce byly přiřazeny omylem.

    Dalším problémem může být přiřazení správného trvalého bydliště k dané obci u pacienta, který
    avšak v obci nepobývá (pouze je tam přihlášen k pobytu) a jeho diagnóza i léčba probíhá jinde.
    Správce i provozovatel ISIN děkují vedení obcí za zpětnou vazbu, neboť jinak takové chyby nelze
    odhalit. Publikování dat na úrovni obcí bylo vedeno snahou o bezbariérový informační servis –
    tato data jsou nyní ve spolupráci se správou základních registrů zpětně validována. Nejde o
    chyby velkého rozsahu, nicméně je nutné je dořešit. Pro starosty všech obcí je nově připravený
    nový internetový dashboard, který umožní rychlou zpětnou kontrolu správnosti.

    Attributes
    ----------

    den: str
        Označení příslušného dne.

    datum: date

    kraj_nuts_kod: str
        Identifikátor kraje podle klasifikace NUTS 3.

    kraj_nazev: str
        Název kraje.

    okres_lau_kod: str
        Identifikátor okresu podle klasifikace LAU 1.

    okres_nazev: str
        Název okresu.

    orp_kod: int
        Kód obce s rozšířenou působností dle číselníku ÚZIS ČR (https://pzu-api.uzis.cz/api/orp).

    orp_nazev: str
        Název obce s rozšířenou působností.

    obec_kod: int
        Kód obce dle číselníku CISOB.

    obec_nazev: str
        Název obce.

    nove_pripady: int
        Celkový počet nově diagnostikovaných za daný den.

    aktivni_pripady: int
        Počet osob pozitivně testovaných na původce onemocnění COVID‑19, které nebyly k danému datu dosud označeny za vyléčené ani nezemřely.

    nove_pripady_65: int
        Počet nově diagnostikovaných za daný den ve věkové skupině 65+.

    nove_pripady_7_dni: int
        Počet nově diagnostikovaných za předchozích 7 dní.

    nove_pripady_14_dni: int
        Počet nově diagnostikovaných za předchozích 14 dní.

    """

    def __init__(self, line: List[str]) :
        self.den: str = line[0]
        self.datum: Optional[date] = date_field(line[1])
        self.kraj_nuts_kod: str = line[2]
        self.kraj_nazev: str = line[3]
        self.okres_lau_kod: str = line[4]
        self.okres_nazev: str = line[5]
        self.orp_kod: int = int_field(line[6])
        self.orp_nazev: str = line[7]
        self.obec_kod: int = int_field(line[8])
        self.obec_nazev: str = line[9]
        self.nove_pripady: int = int_field(line[10])
        self.aktivni_pripady: int = int_field(line[11])
        self.nove_pripady_65: int = int_field(line[12])
        self.nove_pripady_7_dni: int = int_field(line[13])
        self.nove_pripady_14_dni: int = int_field(line[14])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['Obce'] :
        return get_many('obce', Obce, ApiVersion.V2, cache_dir)

