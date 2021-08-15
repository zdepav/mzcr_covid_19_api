from typing import Iterator as _Iterator, Optional as _Optional

from .epidemiologicke_charakteristiky.zakladni_prehled import ZakladniPrehled
from .epidemiologicke_charakteristiky.osoby import Osoby
from .epidemiologicke_charakteristiky.vyleceni import Vyleceni
from .epidemiologicke_charakteristiky.umrti import Umrti
from .epidemiologicke_charakteristiky.hospitalizace import Hospitalizace
from .epidemiologicke_charakteristiky.nakazeni_vyleceni_umrti_testy import NakazeniVyleceniUmrtiTesty
from .epidemiologicke_charakteristiky.kraj_okres_nakazeni_vyleceni_umrti import KrajOkresNakazeniVyleceniUmrti
from .epidemiologicke_charakteristiky.orp import Orp
from .epidemiologicke_charakteristiky.obce import Obce
from .epidemiologicke_charakteristiky.mestske_casti import MestskeCasti
from .epidemiologicke_charakteristiky.incidence_7_14_cr import Incidence_7_14_CR
from .epidemiologicke_charakteristiky.incidence_7_14_kraje import Incidence_7_14_Kraje
from .epidemiologicke_charakteristiky.incidence_7_14_okresy import Incidence_7_14_Okresy

from .testovani.testy_pcr_antigenni import TestyPcrAntigenni
from .testovani.kraj_okres_testy import KrajOkresTesty
from .testovani.prehled_odberovych_mist import PrehledOdberovychMist

from .ockovani.ockovani import Ockovani
from .ockovani.ockovaci_mista import OckovaciMista
from .ockovani.prehled_ockovacich_mist import PrehledOckovacichMist
from .ockovani.ockovani_spotreba import OckovaniSpotreba
from .ockovani.ockovani_distribuce import OckovaniDistribuce
from .ockovani.ockovani_distribuce_sklad import OckovaniDistribuceSklad
from .ockovani.ockovani_registrace import OckovaniRegistrace
from .ockovani.ockovani_rezervace import OckovaniRezervace
from .ockovani.ockovani_profese import OckovaniProfese
from .ockovani.ockovaci_zarizeni import OckovaciZarizeni
from .ockovani.prioritni_skupiny import PrioritniSkupiny

from .ruzne.pomucky import Pomucky

class MzcrCovid19Api :

    _cache_directory_path: _Optional[str]
    
    def __init__(self, cache_directory_path: _Optional[str] = './.cache') :
        self._cache_directory_path = cache_directory_path
    

    def zakladni_prehled(self) -> ZakladniPrehled :
        """ Základní přehled

        Stručný náhled na základní epidemiologická data o pandemii COVID-19 v ČR. Datová sada
        obsahuje aktuální kumulativní počet provedených PCR a antigenních testů (včetně informace za
        předchozí den), potvrzené případy celkem a ve věkové skupině 65+(včetně informace za
        předchozí den), aktivní případy, vyléčené, úmrtí, očkování a hopitalizované pacienty.
        """
        return ZakladniPrehled.get(self._cache_directory_path)


    def osoby(self) -> _Iterator[Osoby] :
        """ Přehled osob s prokázanou nákazou dle hlášení krajských hygienických stanic (v2)

        Datová sada obsahující základní denní incidenční přehled osob s prokázanou nákazou COVID-19
        dle hlášení krajských hygienických stanic (datum hlášení, věk a pohlaví nakažené osoby, KHS,
        informace o místě a zemi nákazy). Datová sada nahrazuje předchozí verzi dostupnou na adrese
        https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/ .
        """
        return Osoby.get(self._cache_directory_path)


    def vyleceni(self) -> _Iterator[Vyleceni] :
        """ Přehled vyléčených dle hlášení krajských hygienických stanic

        Datová sada obsahující záznamy o vyléčených po onemocnění COVID‑19 dle hlášení krajských
        hygienických stanic. S ohledem na fakt, že vykazování vyléčených osob má určité zpoždění
        oproti reálnému stavu z důvodu validace a uzavírání případů krajských hygienických stanic,
        se mohou denní záznamy zpětně měnit právě z důvodu průběžného doplňování. Tento přehled je
        aktualizován vždy jednou týdně ve středu a obsahuje data k předchozí neděli.
        """
        return Vyleceni.get(self._cache_directory_path)


    def umrti(self) -> _Iterator[Umrti] :
        """ Přehled úmrtí dle hlášení krajských hygienických stanic

        Datová sada obsahující záznamy o úmrtích v souvislosti s onemocněním COVID‑19 dle hlášení
        krajských hygienických stanic. Zahrnuje úmrtí osob, které byly pozitivně testovány na
        COVID‑19 (metodou PCR) bez ohledu na to, jaké byly příčiny jejich úmrtí, a k jejichž úmrtí
        došlo v rámci hospitalizace či mimo ni. S ohledem na fakt, že vykazování úmrtí má určité
        zpoždění oproti reálnému stavu z důvodu validace a uzavírání případů krajských hygienických
        stanic, se mohou denní záznamy zpětně měnit právě z důvodu průběžného doplňování. Tento
        přehled je aktualizován vždy jednou týdně ve středu a obsahuje data k předchozí neděli.
        """
        return Umrti.get(self._cache_directory_path)


    def hospitalizace(self) -> _Iterator[Hospitalizace] :
        """ Přehled hospitalizací

        Datová sada obsahující data hospitalizovaných pacientů popisující průběh hospitalizace (aktuální
        a celkový počet hospitalizovaných, rozdělení podle příznaků, rozdělení podle podpůrných
        přístrojů, počet úmrtí).
        """
        return Hospitalizace.get(self._cache_directory_path)


    def nakazeni_vyleceni_umrti_testy(self) -> _Iterator[NakazeniVyleceniUmrtiTesty] :
        """ Celkový (kumulativní) počet osob s prokázanou nákazou dle krajských hygienických stanic
        včetně laboratoří, počet vyléčených, počet úmrtí a provedených testů (v2)

        Datová sada obsahující kumulativní denní počty osob s prokázaným onemocněním COVID-19 dle
        hlášení krajských hygienických stanic včetně laboratoří, denní počty vyléčených po
        onemocnění COVID‑19 dle hlášení krajských hygienických stanic, denní počty úmrtí v
        souvislosti s onemocněním COVID‑19 dle hlášení krajských hygienických stanic a
        hospitalizačních úmrtí, a denní počty provedených testů na onemocnění COVID-19 dle hlášení
        laboratoří. S ohledem na fakt, že vykazování vyléčených osob a úmrtí má určité zpoždění
        oproti reálnému stavu z důvodu validace a uzavírání případů krajských hygienických stanic,
        se mohou denní záznamy zpětně měnit právě z důvodu průběžného doplňování. Datová sada
        nahrazuje předchozí verzi dostupnou na adrese
        https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/ .
        """
        return NakazeniVyleceniUmrtiTesty.get(self._cache_directory_path)


    def kraj_okres_nakazeni_vyleceni_umrti(self) -> _Iterator[KrajOkresNakazeniVyleceniUmrti] :
        """ Přehled epidemiologické situace dle hlášení krajských hygienických stanic podle okresu

        Datová sada podle krajů a okresů ČR obsahující kumulativní denní počty osob s prokázaným
        onemocněním COVID-19 dle validovaných hlášení krajských hygienických stanic, kumulativní
        denní počty vyléčených po onemocnění COVID-19 dle hlášení krajských hygienických stanic a
        kumulativní denní počty úmrtí v souvislosti s onemocněním COVID-19 dle hlášení krajských
        hygienických stanic a hospitalizačních úmrtí. S ohledem na fakt, že vykazování vyléčených
        osob a úmrtí má určité zpoždění oproti reálnému stavu z důvodu validace a uzavírání případů
        krajských hygienických stanic, se mohou denní záznamy zpětně výrazně měnit právě z důvodu
        průběžného doplňování. Nedoporučujeme uvádět aktuální počty aktivních případů na základě
        aktuálních počtů vyléčených osob a úmrtí za poslední dny. Data jsou neúplná a jejich použití
        má za následek zkreslující výsledky. V souladu s rozhodnutím sekce hlavní hygieničky
        Ministerstva zdravotnictví ČR budou na webu COVID-19 publikovány celkové počty aktivních
        případů COVID-19 až zpětně, a to po doplnění a po validaci dat s časovým odstupem 4 týdnů.
        """
        return KrajOkresNakazeniVyleceniUmrti.get(self._cache_directory_path)


    def orp(self) -> _Iterator[Orp] :
        """ Přehled epidemiologické situace dle hlášení krajských hygienických stanic podle ORP

        Obsahem je komplexní přehled základních epidemiologických parametrů (počty diagnostikovaných
        osob s COVID-19, počty aktuálně nakažených, hospitalizovaní pacienti) se zaměřením na
        seniorní zranitelné skupiny obyvatel (kategorie věku 65+, 75+) na geografické úrovni obcí s
        rozšířenou působností (ORP).
        """
        return Orp.get(self._cache_directory_path)


    def obce(self) -> _Iterator[Obce] :
        """ Epidemiologická charakteristika obcí

        Obsah datové sady zahrnuje základní epidemiologické parametry (počty nově diagnostikovaných
        osob s COVID-19, počty aktuálně nakažených) na úrovni obcí ČR.

        Na základě informací z některých malých obcí eviduje správce systému ISIN problémy s
        přiřazením bydliště obyvatel. Jde o chybu ztotožňování bydliště v reálném čase u minority
        případů, kdy není uvedeno bydliště z šetření KHS a jsou dostupná pouze data z laboratoří.
        Bydliště je správně určeno na úrovni kraje a okresu, ale došlo k chybnému přiřazení osob ke
        konkrétní obci. Případy podle všeho patří do velkých měst, a drobné obce byly přiřazeny
        omylem.

        Dalším problémem může být přiřazení správného trvalého bydliště k dané obci u pacienta,
        který avšak v obci nepobývá (pouze je tam přihlášen k pobytu) a jeho diagnóza i léčba
        probíhá jinde. Správce i provozovatel ISIN děkují vedení obcí za zpětnou vazbu, neboť jinak
        takové chyby nelze odhalit. Publikování dat na úrovni obcí bylo vedeno snahou o bezbariérový
        informační servis – tato data jsou nyní ve spolupráci se správou základních registrů zpětně
        validována. Nejde o chyby velkého rozsahu, nicméně je nutné je dořešit. Pro starosty všech
        obcí je nově připravený nový internetový dashboard, který umožní rychlou zpětnou kontrolu
        správnosti.
        """
        return Obce.get(self._cache_directory_path)


    def mestske_casti(self) -> _Iterator[MestskeCasti] :
        """ Epidemiologická charakteristika městských částí hlavního města Prahy

        Obsah datové sady na úrovni městkých části hlavního města Prahy zahrnuje základní
        epidemiologické parametry (počty diagnostikovaných osob s COVID-19, počty aktuálně
        nakažených), které umožní průběžně sledovat základní epidemiologické ukazatele a
        vyhodnocovat trendy na pozadí dat publikovaných pro celou ČR.

        Na základě informací z některých malých obcí eviduje správce systému ISIN problémy s
        přiřazením bydliště obyvatel. Jde o chybu ztotožňování bydliště v reálném čase u minority
        případů, kdy není uvedeno bydliště z šetření KHS a jsou dostupná pouze data z laboratoří.
        Bydliště je správně určeno na úrovni kraje a okresu, ale došlo k chybnému přiřazení osob ke
        konkrétní obci. Případy podle všeho patří do velkých měst, a drobné obce byly přiřazeny
        omylem.

        Dalším problémem může být přiřazení správného trvalého bydliště k dané obci u pacienta,
        který avšak v obci nepobývá (pouze je tam přihlášen k pobytu) a jeho diagnóza i léčba
        probíhá jinde. Správce i provozovatel ISIN děkují vedení obcí za zpětnou vazbu, neboť jinak
        takové chyby nelze odhalit. Publikování dat na úrovni obcí bylo vedeno snahou o bezbariérový
        informační servis – tato data jsou nyní ve spolupráci se správou základních registrů zpětně
        validována. Nejde o chyby velkého rozsahu, nicméně je nutné je dořešit. Pro starosty všech
        obcí je nově připravený nový internetový dashboard, který umožní rychlou zpětnou kontrolu
        správnosti.
        """
        return MestskeCasti.get(self._cache_directory_path)


    def incidence_7_14_cr(self) -> _Iterator[Incidence_7_14_CR] :
        """ Přehled osob s prokázanou nákazou dle krajských hygienických stanic včetně laboratoří za
        7 a 14 dní za ČR

        Datová sada obsahující počty potvrzených případů za posledních 7 a 14 dní za celou ČR včetně
        přepočtu na 100 000 obyvatel. Pro přepočet na 100 000 obyvatel je použita otevřená datová
        sada Obyvatelstvo podle pětiletých věkových skupin a pohlaví v krajích a okresech
        (https://www.czso.cz/csu/czso/obyvatelstvo-podle-petiletych-vekovych-skupin-a-pohlavi-v-krajich-a-okresech).
        """
        return Incidence_7_14_CR.get(self._cache_directory_path)


    def incidence_7_14_kraje(self) -> _Iterator[Incidence_7_14_Kraje] :
        """ Přehled osob s prokázanou nákazou dle krajských hygienických stanic včetně laboratoří za
        7 a 14 dní podle krajů

        Datová sada obsahující počty potvrzených případů za posledních 7 a 14 dní za kraje ČR včetně
        přepočtu na 100 000 obyvatel. Pro přepočet na 100 000 obyvatel je použita otevřená datová
        sada Obyvatelstvo podle pětiletých věkových skupin a pohlaví v krajích a okresech
        (https://www.czso.cz/csu/czso/obyvatelstvo-podle-petiletych-vekovych-skupin-a-pohlavi-v-krajich-a-okresech).
        """
        return Incidence_7_14_Kraje.get(self._cache_directory_path)


    def incidence_7_14_okresy(self) -> _Iterator[Incidence_7_14_Okresy] :
        """ Přehled osob s prokázanou nákazou dle krajských hygienických stanic včetně laboratoří za
        7 a 14 dní podle okresů

        Datová sada obsahující počty potvrzených případů za posledních 7 a 14 dní za okresy ČR
        včetně přepočtu na 100 000 obyvatel. Pro přepočet na 100 000 obyvatel je použita otevřená
        datová sada Obyvatelstvo podle pětiletých věkových skupin a pohlaví v krajích a okresech
        (https://www.czso.cz/csu/czso/obyvatelstvo-podle-petiletych-vekovych-skupin-a-pohlavi-v-krajich-a-okresech).
        """
        return Incidence_7_14_Okresy.get(self._cache_directory_path)


    def testy_pcr_antigenni(self) -> _Iterator[TestyPcrAntigenni] :
        """ Přehled provedených testů podle typu a indikace

        Datová sada obsahující denní počty provedených testů s rozlišením na PCR testy a antigenní
        testy na onemocnění COVID-19 dle hlášení laboratoří. Dále jsou v sadě uvedeny počty testů
        dle indikace (diagnostické indikace, epidemiologické indikace, preventivní a plošné
        testování, ostatní), pozitivní záchyty dle indikace testu a pozitivní záchyty dle typu testu
        (symptomy jsou objektivně vyšetřeny u indikovaných osob, v rámci plošného testování jde o
        vyjádření subjektivního posouzení testovaného). Zdrojem dat je centrální Informační systém
        infekčních nemocí (ISIN). Primární data byla analyticky zpracována a následně transformována
        do podoby publikovatelné online týmem ÚZIS ČR.
        """
        return TestyPcrAntigenni.get(self._cache_directory_path)


    def kraj_okres_testy(self) -> _Iterator[KrajOkresTesty] :
        """ Celkový (kumulativní) počet provedených testů podle krajů a okresů ČR

        Datová sada obsahující přírůstkové a kumulativní denní počty provedených PCR testů s korekcí
        na opakovaně pozitivní (kontrolní) testy, a to bez rozdílu způsobu úhrady (tedy včetně
        samoplátců), na COVID 19 za celou ČR podle hlášení laboratoří (rychlotesty nejsou do
        přehledu zařazeny). Tento přehled je k dispozici od 1. srpna 2020 z důvodu úplnosti
        nahlášených dat jednotlivými laboratořemi na individuální úrovni. V předchozím období
        existuje riziko neúplnosti těchto individuálních dat a proto do 31. července vycházíme pouze
        z dat agregovaných, která však neumožňují složitější analytické výpočty.
        """
        return KrajOkresTesty.get(self._cache_directory_path)


    def prehled_odberovych_mist(self) -> _Iterator[PrehledOdberovychMist] :
        """ Odběrová místa v ČR

        Datová sada poskytuje seznam odběrových míst v ČR, kde jsou prováděny PCR a antigenní testy
        na onemocnění COVID-19. Součástí publikovaného seznamu nejsou odběrová místa ve
        zdravotnických zařízeních, kde jsou prováděny testy před přijetím pacienta v souvislosti s
        poskytováním neodkladné péče. Mobilní odběrové týmy mají kapacitu pevně nastavenu (na
        hodnotu 20), protože není možné přesně určit tuto kapacitu.
        """
        return PrehledOdberovychMist.get(self._cache_directory_path)


    def ockovani(self) -> _Iterator[Ockovani] :
        """ Přehled vykázaných očkování podle krajů ČR

        Datová sada poskytuje agregovaná data o vykázaných očkováních na úrovni krajů ČR. Každý
        řádek přehledu popisuje počet vykázaných očkování v daném dni, za věkovou skupinu, s
        použitím vybrané očkovací látky a ve vybraném kraji. Za jeden den tedy přehled obsahuje
        maximálně X řádků, kde X = počet krajů (14) x počet věkových skupin (15) x počet druhů
        očkovacích látek (v okamžik publikace 4) = 840. Data jsou aktualizována k času 20.00 h
        předchozího dne a mohou se zpětně mírně měnit z důvodu průběžného doplňování.
        """
        return Ockovani.get(self._cache_directory_path)


    def ockovaci_mista(self) -> _Iterator[OckovaciMista] :
        """ Přehled vykázaných očkování podle očkovacích míst ČR

        Datová sada poskytuje řádková data o vykázaných očkováních na jednotlivých očkovacích
        místech ČR. Každý řádek přehledu popisuje jedno vykázané očkování v daném dni a věkové
        skupině, s použitím vybrané očkovací látky, na konkrétním očkovacím místu a ve vybraném
        kraji.
        """
        return OckovaciMista.get(self._cache_directory_path)


    def prehled_ockovacich_mist(self) -> _Iterator[PrehledOckovacichMist] :
        """ Očkovací místa v ČR

        Datová sada poskytuje seznam veřejných očkovacích míst v ČR, kde jsou podávány očkovací
        látky proti onemocnění COVID-19.
        """

        return PrehledOckovacichMist.get(self._cache_directory_path)


    def ockovani_spotreba(self) -> _Iterator[OckovaniSpotreba] :
        """ Přehled spotřeby podle očkovacích míst ČR

        Datová sada obsahuje přehled spotřeby očkovacích látek (použité a znehodnocené ampulky)
        proti onemocnění COVID-19 v očkovacích místech v ČR. Každý záznam (řádek) datové sady udává
        počet použitých a znehodnocených ampulek dané očkovací látky na daném očkovacím místě v daný
        den.
        """
        return OckovaniSpotreba.get(self._cache_directory_path)


    def ockovani_distribuce(self) -> _Iterator[OckovaniDistribuce] :
        """ Přehled distribuce očkovacích látek v ČR

        Datová sada obsahuje přehled distribuce očkovacích látek proti onemocnění COVID-19 do
        očkovacích míst v ČR. Každý záznam (řádek) datové sady udává počet ampulek dané očkovací
        látky, která byla daným očkovacím místem v daný den přijata nebo vydána.
        """
        return OckovaniDistribuce.get(self._cache_directory_path)


    def ockovani_distribuce_sklad(self) -> _Iterator[OckovaniDistribuceSklad] :
        """ Přehled distribuce očkovacích látek v ČR z centrálního skladu

        Datová sada obsahuje přehled distribuce očkovacích látek proti onemocnění COVID-19 v rámci
        centrálního skladu (příjem na centrální skladu a výdej do očkovacích míst v ČR). Každý
        záznam (řádek) datové sady udává počet ampulek dané očkovací látky, která byla daným
        očkovacím místem v daný den přijata nebo vydána.
        """
        return OckovaniDistribuceSklad.get(self._cache_directory_path)


    def ockovani_registrace(self) -> _Iterator[OckovaniRegistrace] :
        """ Přehled registrací podle očkovacích míst ČR

        Datová sada poskytuje přehled vytvořených registrací v centrálním rezervačním systému na
        očkování proti onemocnění COVID-19 (https://registrace.mzcr.cz/). Záznamy (řádky) datové
        sady popisují jednotlivé anonymizované registrace, které byly vytvořeny na dané očkovací
        místo v daný den. Do datové sady spadají také osoby, které již byly očkovány. Registrovaná
        osoba je definována tak, že spadá do jedné s následujících skupin:

        (i) osoba je registrovaná a čeká na přidělení možnosti výběru termínu očkování,

        (ii) osoba obdržela možnost výběru termínu očkování,

        (iii) osoba provedla výběr termínu a má tedy rezervaci.

        Popis procesu rezervace a registrace:

        (1) Osoba se registruje v centrálním rezervačním systému na očkování.

        (2) Probíhá proces ztotožnění proti centrálnímu registru obyvatel.

        (3) Po ověření totožnosti čeká osoba na přidělení možnosti výběru termínu (stav před
        závorou).

        (4) Po přidělení možnosti výběru termínu si osoba vybírá vhodný termín (stav za závorou).

        (5) Po výběru termínu má daná osoba provedenu rezervaci termínu na očkování.

        (6) Po provedení očkování zůstává záznam v datové sadě s blokovanou registrací (zablokovano
        = ANO) a současně je uveden důvod blokace (blokace_duvod = Ztotožněn, ale již vakcinován).
        """
        return OckovaniRegistrace.get(self._cache_directory_path)


    def ockovani_rezervace(self) -> _Iterator[OckovaniRezervace] :
        """ Přehled rezervací podle očkovacích míst ČR

        Datová sada poskytuje přehled volné a maximální kapacity očkovacích míst v jednotlivých
        dnech podle informací z centrálního rezervačního systému na očkování proti onemocnění
        COVID-19 (https://reservatic.com/ockovani). Každý záznam (řádek) datové sady udává volnou a
        maximální kapacitu daného očkovacího místa v daný den.
        """
        return OckovaniRezervace.get(self._cache_directory_path)


    def ockovani_profese(self) -> _Iterator[OckovaniProfese] :
        """ Přehled vykázaných očkování podle profesí (očkovací místo, bydliště očkovaného)

        Datová sada poskytuje řádková data o vykázaných očkováních na jednotlivých očkovacích
        místech ČR. Každý řádek přehledu popisuje jedno vykázané očkování v daném dni a indikační
        skupině profese, s použitím dané dávky očkovací látky, na konkrétním očkovacím místu a ve
        vybraném kraji.
        """
        return OckovaniProfese.get(self._cache_directory_path)


    def ockovaci_zarizeni(self) -> _Iterator[OckovaciZarizeni] :
        """ Očkovací zařízení

        Datová sada poskytuje seznam očkovacích zařízení v ČR jako doplnění seznamu očkovacích míst,
        kde jsou podávány očkovací látky proti onemocnění COVID-19. Jedná se především o praktické
        lékaře, ale i další, kde se očkování provádí.
        """
        return OckovaciZarizeni.get(self._cache_directory_path)


    def prioritni_skupiny(self) -> _Iterator[PrioritniSkupiny] :
        """ Číselník prioritních skupin očkování

        Seznam prioritních skupin pro rozdělení očkovaných osob na základě prioritizačního systému
        Ministerstvem zdravotnictví ČR, který je použit v datové sadě COVID-19: Přehled vykázaných
        očkování podle profesí.
        """
        return PrioritniSkupiny.get(self._cache_directory_path)


    def pomucky(self) -> _Iterator[Pomucky] :
        """ Přehled distribuce ochranného materiálu dle krajů ČR (v2)

        Datová sada obsahující aktuální přehled o počtech kusů ochranného materiálu k danému dni
        který byl distribuován do jednotlivých krajů v ČR (brýle, dezinfekce, roušky, respirátory,
        ...). Datová sada nahrazuje předchozí verzi dostupnou na adrese
        https://onemocneni-aktualne.mzcr.cz/api/v1/covid-19/ .
        """
        return Pomucky.get(self._cache_directory_path)

