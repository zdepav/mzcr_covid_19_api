from ..api import get_many, ApiVersion, bool_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class OckovaniRegistrace:
    """ Přehled registrací podle očkovacích míst ČR

    Datová sada poskytuje přehled vytvořených registrací v centrálním rezervačním systému na
    očkování proti onemocnění COVID-19 (https://registrace.mzcr.cz/). Záznamy (řádky) datové sady
    popisují jednotlivé anonymizované registrace, které byly vytvořeny na dané očkovací místo v daný
    den. Do datové sady spadají také osoby, které již byly očkovány. Registrovaná osoba je
    definována tak, že spadá do jedné s následujících skupin:
    
    (i) osoba je registrovaná a čeká na přidělení možnosti výběru termínu očkování,
    
    (ii) osoba obdržela možnost výběru termínu očkování,
    
    (iii) osoba provedla výběr termínu a má tedy rezervaci.

    Popis procesu rezervace a registrace:
    
    (1) Osoba se registruje v centrálním rezervačním systému na očkování.
    
    (2) Probíhá proces ztotožnění proti centrálnímu registru obyvatel.
    
    (3) Po ověření totožnosti čeká osoba na přidělení možnosti výběru termínu (stav před závorou).
    
    (4) Po přidělení možnosti výběru termínu si osoba vybírá vhodný termín (stav za závorou).
    
    (5) Po výběru termínu má daná osoba provedenu rezervaci termínu na očkování.
    
    (6) Po provedení očkování zůstává záznam v datové sadě s blokovanou registrací (zablokovano =
    ANO) a současně je uveden důvod blokace (blokace_duvod = Ztotožněn, ale již vakcinován).


    Attributes
    ----------

    datum: date
        Den, kdy byla registrace v centrálním registračním systému na očkování proti onemocnění
        COVID-19 vytvořena.

    ockovaci_misto_id: str
        Jednoznačný identifikátor očkovacího místa.

    ockovaci_misto_nazev: str
        Název očkovacího místa.

    kraj_nuts_kod: str
        Identifikátor kraje podle klasifikace NUTS 3, ve kterém se nachází očkovací místo.

    kraj_nazev: str
        Název kraje podle klasifikace NUTS 3, ve kterém se nachází očkovací místo.

    vekova_skupina: str
        Věková skupina, do které spadá uživatel vytvářející registraci na očkování proti onemocnění
        COVID-19.

    povolani: str
        Povolání uživatele vytvářejícího registraci na očkování proti onemocnění COVID-19 podle
        Národního registru zdravotnických pracovníků.

    stat: str
        Stát, ze kterého je uživatel vytvářející registraci na očkování proti onemocnění COVID-19.

    rezervace: bool
        Příznak, zda uživatel již obdržel rezervaci termínu na očkování proti onemocnění COVID-19.

    datum_rezervace: date
        Datum rezervace na očkování proti onemocnění COVID-19.

    zavora_status: str
        Určení, v jakém stavu se nachází registrace dané osoby:

        1. stav „před závorou“ = osoba je registrovaná v systému a čeká na přidělení možnosti výběru
        termínu na očkování

        2. stav „za závorou“ = osoba je registrovaná v systému a má možnost výběru termínu na
        očkování

        3. stav „zablokován“ = osoba byla zablokována

        4. stav „vrácen před závoru“ = osoba měla možnost výběru termínu, ale nevyužila ji

    prioritni_skupina: str
        Určení, do jaké prioritní skupiny byla osoba přiřazena (u jednoho záznamu je právě jedna
        prioritní skupina).

    zablokovano: bool
        Stav, zda byla registrace zablokována.

    duvod_blokace: str
        Zdůvodnění, proč byla očkovaná osoba zablokována.

        1. Vytvoření novější registrace (Procedura při vytváření registrace) - V okamžiku, kdy je
        vytvářena nová registrace, je předchozí registrace se stejným identifikátorem zablokována,
        pokud u ní není rezervace.

        2. Existence předchozí registrace s rezervací (Procedura při vytváření registrace) - V
        okamžiku, kdy je vytvářena nová registrace, a je nalezena předchozí nezablokovaná registrace
        se stejným identifikátorem s platnou rezervací, je nově vytvářená registrace zablokovaná.

        3. 5x špatně zadané PIN2 (Aplikační rozhraní) - Pokud uživatel při pokusu o vstup zadá 5x
        špatné PIN 2, je registrace zablokována.

        4. Již existuje rezervace (Aplikační rozhraní) - Po vytvoření rezervace je registrace
        zablokována. V případě zrušení rezervace bude registrace odblokována.

        5. Vyřazení ze hry (Závora) - Při pasivním chování uživatele, kterému bylo umožněno vybrat
        si termín očkování (stav „za závorou“, jsou zasílány SMS notifikace pro připomenutí. Pokud
        si uživatel ani po zaslání 9 notifikací nevybere termín, je automaticky zablokován.

        6. Registrace nebyla ztotožněna (Synchronizace s centrálními registry) - V případě, že není
        registrace ztotožněna.

        7. Ztotožněn, ale již vakcinován (Synchronizace s centrálními registry) - V případě, že
        osoba v registraci byla ztotožněna, ale již u ní byla zahájena vakcinace.

        8. Na žádost (Ruční administrace) - Pokud si uživatel v detailu registrace registraci
        zruší/vynuluje nebo změní své údaje.

        9. Nalezení pozitivního PCR testu na COVID-19 (Procedura při kontrole COVID-19 pozitiv) -
        Při ztotožňování a následně 1x denně je kontrolováno, zda nemá registrovaná osoba PCR test
        na COVID-19 pozitivní v posledních 90 dnech. Pokud ano, je dočasně zablokována.

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.ockovaci_misto_id: str = line[1]
        self.ockovaci_misto_nazev: str = line[2]
        self.kraj_nuts_kod: str = line[3]
        self.kraj_nazev: str = line[4]
        self.vekova_skupina: str = line[5]
        self.povolani: str = line[6]
        self.stat: str = line[7]
        self.rezervace: bool = bool_field(line[8])
        self.datum_rezervace: Optional[date] = date_field(line[9])
        self.zavora_status: str = line[10]
        self.prioritni_skupina: str = line[11]
        self.zablokovano: bool = bool_field(line[12])
        self.duvod_blokace: str = line[13]


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['OckovaniRegistrace'] :
        return get_many('ockovani-registrace', OckovaniRegistrace, ApiVersion.V2, cache_dir)

