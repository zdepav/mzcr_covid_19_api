from ..api import get_many, ApiVersion, int_field, bool_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class OckovaniProfese:
    """ Přehled vykázaných očkování podle profesí (očkovací místo, bydliště očkovaného)

    Datová sada poskytuje řádková data o vykázaných očkováních na jednotlivých očkovacích místech
    ČR. Každý řádek přehledu popisuje jedno vykázané očkování v daném dni a indikační skupině
    profese, s použitím dané dávky očkovací látky, na konkrétním očkovacím místu a ve vybraném
    kraji.

    Attributes
    ----------

    datum: date
        Datum, ve kterém byla očkování v daném kraji provedena.

    vakcina: str
        Název očkovací látky.

    kraj_nuts_kod: str
        Identifikátor kraje podle klasifikace NUTS 3, ve kterém se nachází očkovací místo.

    kraj_nazev: str
        Název kraje, ve kterém se nachází očkovací místo.

    zarizeni_kod: str
        Kód zdravotnického zařízení, ve kterém se nachází očkovací místo (podle číselníku
        poskytovatelů zdravotních služeb na úrovni jednotlivých zařízení).

    zarizeni_nazev: str
        Název zdravotnického zařízení, ve kterém se nachází očkovací místo.

    poradi_davky: int
        Pořadí dávky (první, druhá) danou očkovací látkou.

    indikace_zdravotnik: bool
        Určení, zda očkovaná osoba spadá mezi zdravotnické pracovníky (zejména nemocnice, ZZS,
        primární ambulantní péče, farmaceuti, laboratoře vyšetřující COVID-19, zdravotníci v
        sociálních službách) nebo do oblasti ochrany veřejného zdraví.

    indikace_socialni_sluzby: bool
        Určení, zda očkovaná osoba spadá mezi pracovníky nebo klienty v sociálních službách.

    indikace_ostatni: bool
        Určení, zda očkovaná osoba spadá mezi pracovníky kritické infrastruktury, které zahrnují
        integrovaný záchranný systém, pracovníky energetiky, vládu a krizové štáby (osoba není
        začleněna v indikačních skupinách zdravotník nebo sociální služby).

    indikace_pedagog: bool
        Určení, zda očkovaná osoba spadá mezi pedagogické pracovníky.

    indikace_skolstvi_ostatni: bool
        Určení, zda očkovaná osoba spadá mezi ostatní pracovníky ve školství.

    indikace_bezpecnostni_infrastruktura: bool
        Určení, zda očkovaná osoba spadá mezi zaměstnance Ministerstva obrany nebo bezpečnostní
        sbory.

    indikace_chronicke_onemocneni: bool
        Určení, zda očkovaná osoba spadá mezi chronicky nemocné (hematoonkologické onemocnění,
        onkologické onemocnění (solidní nádory), závažné akutní nebo dlouhodobé onemocnění srdce,
        závažné dlouhodobé onemocnění plic, diabetes mellitus, obezita, závažné dlouhodobé
        onemocnění ledvin, závažné dlouhodobé onemocnění jater, stav po transplantaci nebo na čekací
        listině, hypertenze, závažné neurologické nebo neuromuskulární onemocnění, vrozený nebo
        získaný kognitivní deficit, vzácné genetické onemocnění, závažné oslabení imunitního
        systému, jiné závažné onemocnění).

    vekova_skupina: str
        Rozdělení očkovaných osob podle věku do skupin.

    orp_bydliste: str
        Bydliště (na úrovni názvu obce s rozšířenou působností) očkované osoby.

    orp_bydliste_kod: int
        Bydliště (na úrovni kódu obce s rozšířenou působností) podle číselníku ÚZIS ČR
        (https://pzu-api.uzis.cz/api/orp) očkované osoby.

    prioritni_skupina_kod: int
        Rozdělení očkovaných osob do prioritních skupin na základě prioritizačního systému
        Ministerstvem zdravotnictví ČR, které určuje na základě věku, zdravotní anamnézy a profese
        časový harmonogram očkování. Každá osoba spadá právě do jedné prioritní skupiny. Číselník
        prioritních skupin je dostupný na adrese
        https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/prioritni-skupiny.csv .

    pohlavi: str
        V případě neuvedení pohlaví u vykázaného očkování se jedná o cizince, u kterého není možné
        prostřednictvím centrálních registrů pohlaví identifikovat.

    zrizovatel_kod: int
        Kód zřizovatele očkovacího místa.

    zrizovatel_nazev: str
        Název zřizovatele očkovacího místa.

    vakcina_kod: str
        Kód očkovací látky podle klasifikace ÚZIS ČR.

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.vakcina: str = line[1]
        self.kraj_nuts_kod: str = line[2]
        self.kraj_nazev: str = line[3]
        self.zarizeni_kod: str = line[4]
        self.zarizeni_nazev: str = line[5]
        self.poradi_davky: int = int_field(line[6])
        self.indikace_zdravotnik: bool = bool_field(line[7])
        self.indikace_socialni_sluzby: bool = bool_field(line[8])
        self.indikace_ostatni: bool = bool_field(line[9])
        self.indikace_pedagog: bool = bool_field(line[10])
        self.indikace_skolstvi_ostatni: bool = bool_field(line[11])
        self.indikace_bezpecnostni_infrastruktura: bool = bool_field(line[12])
        self.indikace_chronicke_onemocneni: bool = bool_field(line[13])
        self.vekova_skupina: str = line[14]
        self.orp_bydliste: str = line[15]
        self.orp_bydliste_kod: int = int_field(line[16])
        self.prioritni_skupina_kod: int = int_field(line[17])
        self.pohlavi: str = line[18]
        self.zrizovatel_kod: int = int_field(line[19])
        self.zrizovatel_nazev: str = line[20]
        self.vakcina_kod: str = line[21]


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['OckovaniProfese'] :
        return get_many('ockovani-profese', OckovaniProfese, ApiVersion.V2, cache_dir)

