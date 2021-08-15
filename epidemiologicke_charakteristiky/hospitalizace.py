from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class Hospitalizace:
    """ Přehled hospitalizací

    Datová sada obsahující data hospitalizovaných pacientů popisující průběh hospitalizace (aktuální
    a celkový počet hospitalizovaných, rozdělení podle příznaků, rozdělení podle podpůrných
    přístrojů, počet úmrtí).

    Attributes
    ----------

    datum: date

    pacient_prvni_zaznam: int
        Počet osob, které byly poprvé hospitalizovány.

    kum_pacient_prvni_zaznam: int
        Celkový počet hospitalizovaných osob.

    pocet_hosp: int
        Aktuální počet hospitalizovaných osob.

    stav_bez_priznaku: int
        Počet pacientů bez příznaků na základě subjektivního hodnocení lékaře.

    stav_lehky: int
        Počet pacientů v lehkém stavu na základě subjektivního hodnocení lékaře.

    stav_stredni: int
        Počet pacientů ve středně vážném stavu na základě subjektivního hodnocení lékaře.

    stav_tezky: int
        Počet pacientů v těžkém stavu na základě subjektivního hodnocení lékaře.

    jip: int
        Počet pacientů umístěným na jednotce intenzivní péče (JIP).

    kyslik: int
        Počet pacientů – O2.

    hfno: int
        Počet pacientů – HFNO (vysokoprůtoková nosní oxygenoterapie).

    upv: int
        Počet pacientů – UPV (umělá plicní ventilace).

    ecmo: int
        Počet pacientů – ECMO (mimotělní membránová oxygenace (pokročilá metoda podpory životních
        funkcí)).

    tezky_upv_ecmo: int
        Počet pacientů v těžkém stavu nebo s vysoce intenzivní péčí (UPV, ECMO).

    umrti: int
        Počet pacientů, kteří v daný den zemřeli.

    kum_umrti: int
        Celkový počet pacientu, kteří zemřeli.

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.pacient_prvni_zaznam: int = int_field(line[1])
        self.kum_pacient_prvni_zaznam: int = int_field(line[2])
        self.pocet_hosp: int = int_field(line[3])
        self.stav_bez_priznaku: int = int_field(line[4])
        self.stav_lehky: int = int_field(line[5])
        self.stav_stredni: int = int_field(line[6])
        self.stav_tezky: int = int_field(line[7])
        self.jip: int = int_field(line[8])
        self.kyslik: int = int_field(line[9])
        self.hfno: int = int_field(line[10])
        self.upv: int = int_field(line[11])
        self.ecmo: int = int_field(line[12])
        self.tezky_upv_ecmo: int = int_field(line[13])
        self.umrti: int = int_field(line[14])
        self.kum_umrti: int = int_field(line[15])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['Hospitalizace'] :
        return get_many('hospitalizace', Hospitalizace, ApiVersion.V2, cache_dir)

