from ..api import get_many, ApiVersion, int_field
from typing import Iterator, List, Optional

class Pomucky:
    """ Přehled distribuce ochranného materiálu dle krajů ČR (v2)

    Datová sada obsahující aktuální přehled o počtech kusů ochranného materiálu k danému dni, který
    byl distribuován do jednotlivých krajů v ČR (brýle, dezinfekce, roušky, respirátory, ...).
    Datová sada nahrazuje předchozí verzi dostupnou na adrese
    https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/ .

    Attributes
    ----------

    pomucka: str
        Typ ochranného materiálu.

    kraj_nuts_kod: str
        Identifikátor kraje podle klasifikace NUTS 3, kam byl ochranný materiál distribuován.

    mnozstvi: int
        Množství distribuovaného ochranného materiálu.

    """

    def __init__(self, line: List[str]) :
        self.pomucka: str = line[0]
        self.kraj_nuts_kod: str = line[1]
        self.mnozstvi: int = int_field(line[2])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['Pomucky'] :
        return get_many('pomucky', Pomucky, ApiVersion.V2, cache_dir)

