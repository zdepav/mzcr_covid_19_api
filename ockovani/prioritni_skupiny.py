from ..api import get_many, ApiVersion, int_field
from typing import Iterator, List, Optional

class PrioritniSkupiny:
    """ Číselník prioritních skupin očkování

    Seznam prioritních skupin pro rozdělení očkovaných osob na základě prioritizačního systému
    Ministerstvem zdravotnictví ČR, který je použit v datové sadě COVID-19: Přehled vykázaných
    očkování podle profesí.

    Attributes
    ----------

    kod: int
        Kód prioritní skupiny.

    hodnota: str
        Název prioritní skupiny.

    """

    def __init__(self, line: List[str]) :
        self.kod: int = int_field(line[0])
        self.hodnota: str = line[1]


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['PrioritniSkupiny'] :
        return get_many('prioritni-skupiny', PrioritniSkupiny, ApiVersion.V2, cache_dir)

