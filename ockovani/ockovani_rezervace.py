from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class OckovaniRezervace:
    """ Přehled rezervací podle očkovacích míst ČR

    Datová sada poskytuje přehled volné a maximální kapacity očkovacích míst v jednotlivých dnech
    podle informací z centrálního rezervačního systému na očkování proti onemocnění COVID-19
    (https://reservatic.com/ockovani). Každý záznam (řádek) datové sady udává volnou a maximální
    kapacitu daného očkovacího místa v daný den.

    Attributes
    ----------

    datum: date
        Datum, ke kterému se vztahují volné a maximální kapacity očkovacího místa podle centrálního
        registračnímu systému na očkování proti onemocnění COVID-19.

    ockovaci_misto_id: str
        Jednoznačný identifikátor očkovacího místa.

    ockovaci_misto_nazev: str
        Název očkovacího místa

    kraj_nuts_kod: str
        Identifikátor kraje podle klasifikace NUTS 3, ve kterém se nachází očkovací místo.

    kraj_nazev: str
        Název kraje podle klasifikace NUTS 3, ve kterém se nachází očkovací místo.

    volna_kapacita: int
        Volná kapacita očkovacího místa v daný den.

    maximalni_kapacita: int
        Maximální kapacita očkovacího místa v daný den.

    kalendar_ockovani: str
        Identifikátor, zda se jedná o rezervaci na první dávku (hodnota V1), druhou dávku (hodnota
        V2) nebo jde o přednostní rezervaci (např. lékařů) (hodnota VX).

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.ockovaci_misto_id: str = line[1]
        self.ockovaci_misto_nazev: str = line[2]
        self.kraj_nuts_kod: str = line[3]
        self.kraj_nazev: str = line[4]
        self.volna_kapacita: int = int_field(line[5])
        self.maximalni_kapacita: int = int_field(line[6])
        self.kalendar_ockovani: str = line[7]


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['OckovaniRezervace'] :
        return get_many('ockovani-rezervace', OckovaniRezervace, ApiVersion.V2, cache_dir)

