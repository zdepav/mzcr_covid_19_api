from ..api import get_one, ApiVersion, int_field, date_field
from datetime import date
from typing import List, Optional

class ZakladniPrehled :
    """ Základní přehled

    Stručný náhled na základní epidemiologická data o pandemii COVID-19 v ČR. Datová sada obsahuje
    aktuální kumulativní počet provedených PCR a antigenních testů (včetně informace za předchozí
    den), potvrzené případy celkem a ve věkové skupině 65+(včetně informace za předchozí den),
    aktivní případy, vyléčené, úmrtí, očkování a hopitalizované pacienty.

    Attributes
    ----------

    datum: date
        Datum vytvoření aktualizace.

    provedene_testy_celkem: int
        Celkový počet provedených PCR testů na původce onemocnění COVID‑19 za celou ČR (kumulativně
        od 27. 1. 2020) podle hlášení laboratoří (rychlotesty nejsou do přehledu zařazeny).
        S ohledem na fakt, že hlášení o provedených testech mají určité zpoždění oproti reálnému
        stavu, se mohou denní záznamy zpětně mírně měnit právě z důvodu průběžného doplňování.

    potvrzene_pripady_celkem: int
        Celkový počet osob dosud pozitivně testovaných na původce onemocnění COVID‑19 (kumulativně
        od 1. 3. 2020) dle hlášení KHS a dle pozitivních nálezů laboratoří, které jsou určeny pro
        další šetření. S ohledem na fakt, že u publikovaných dat probíhá validace a průběžné
        doplňování hlášení, jsou přehledy osob s laboratorně prokázaným onemocněním COVID‑19 dle
        hlášení KHS a laboratoří uváděny k datu hlášení do systému a historicky se nemění (případné
        opravy tedy nejsou do již publikovaných výstupů promítnuty).

    aktivni_pripady: int
        Počet osob pozitivně testovaných na původce onemocnění COVID‑19, které nebyly k danému datu
        dosud označeny za vyléčené (dva negativní testy) ani nezemřely.

    vyleceni: int
        Celkový počet osob, které byly pozitivně laboratorně testovány metodou PCR na přítomnost
        původce onemocnění COVID‑19 (bez ohledu na klinický průběh nemoci a případně aplikovanou
        léčbu), a následně u nich bylo dvakrát provedeno toto laboratorní testování s negativním
        výsledkem.

    umrti: int
        Celkový počet úmrtí osob s onemocněním COVID‑19 zahrnuje všechna úmrtí osob, které byly
        pozitivně testovány na COVID‑19 (metodou PCR) bez ohledu na to, jaké byly příčiny jejich
        úmrtí, zda k jejichž úmrtí došlo v rámci hospitalizace či mimo ni. S ohledem na fakt, že
        vykazování úmrtí má určité zpoždění oproti reálnému stavu z důvodu validace a uzavírání
        případů krajských hygienických stanic, se mohou denní záznamy zpětně měnit právě z důvodu
        průběžného doplňování.

    aktualne_hospitalizovani: int
        Aktuální počet hospitalizovaných osob s laboratorně prokázaným onemocněním COVID‑19 dle
        průběžného hlášení nemocnic bez ohledu na důvody hospitalizace.

    provedene_testy_vcerejsi_den: int
        Celkový počet provedených PCR testů (včetně opakovaných testů u stejné osoby a bez rozdílu
        způsobu úhrady, tedy včetně samoplátců) na původce onemocnění COVID‑19 za celou ČR v
        předchozím dni.

    potvrzene_pripady_vcerejsi_den: int
        Celkový počet osob dosud pozitivně testovaných na původce onemocnění COVID‑19 v předchozím
        dni dle hlášení KHS a dle pozitivních nálezů laboratoří, které jsou určeny pro další
        šetření.

    potvrzene_pripady_dnesni_den: int
        Celkový počet osob dosud pozitivně testovaných na původce onemocnění COVID‑19 v tomto dni
        dle hlášení KHS a dle pozitivních nálezů laboratoří, které jsou určeny pro další šetření.

    provedene_testy_vcerejsi_den_datum: date
        Datum přírůstku provedených testů za poslední uzavřený den.

    potvrzene_pripady_vcerejsi_den_datum: date
        Datum přírůstku odhalených pozitivních případů za poslední uzavřený den.

    potvrzene_pripady_dnesni_den_datum: date
        Datum průbežného přírůstku odhalených pozitivních případů za poslední neuzavřený den.

    provedene_antigenni_testy_celkem: int
        Celkový počet provedených antigenních testů na původce onemocnění COVID-19 za celou ČR. S
        ohledem na fakt, že hlášení o provedených testech mají určité zpoždění oproti reálnému
        stavu, se mohou denní záznamy zpětně mírně měnit právě z důvodu průběžného doplňování.

    provedene_antigenni_testy_vcerejsi_den: int
        Celkový počet provedených antigenních testů na původce onemocnění COVID-19 za celou ČR v
        předchozím dni.

    provedene_antigenni_testy_vcerejsi_den_datum: date
        Datum přírůstku provedených antigenních testů za poslední uzavřený den.

    vykazana_ockovani_celkem: int
        Celkový počet vykázaných očkování proti onemocnění COVID-19 za celou ČR. Data se mohou
        zpětně mírně měnit z důvodu průběžného doplňování.

    vykazana_ockovani_vcerejsi_den: int
        Celkový počet vykázaných očkování proti onemocnění COVID-19 za celou ČR v předchozím dni.

    vykazana_ockovani_vcerejsi_den_datum: date
        Datum přírůstku vykázaných očkování za poslední uzavřený den.

    potvrzene_pripady_65_celkem: int
        Celkový počet odhalených pozitivních případů ve věkové kategorii 65+.

    potvrzene_pripady_65_vcerejsi_den: int
        Počet odhalených pozitivních případů ve věkové kategorii 65+ za poslední uzavřený den.

    potvrzene_pripady_65_vcerejsi_den_datum: date
        Datum přírůstku odhalených pozitivních případů ve věkové kategorii 65+ za poslední uzavřený
        den.

    ockovane_osoby_celkem: int
        Celkový počet vykázaných očkovaných osob s alespoň 1 dávkou proti onemocnění COVID-19 za
        celou ČR. Data se mohou zpětně mírně měnit z důvodu průběžného doplňování.

    ockovane_osoby_vcerejsi_den: int
        Celkový počet vykázaných očkovaných osob s alespoň 1 dávkou proti onemocnění COVID-19 za
        celou ČR v předchozím dni.

    ockovane_osoby_vcerejsi_den_datum: date
        Datum přírůstku vykázaných očkovaných osob s alespoň 1 dávkou za poslední uzavřený den.

    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.provedene_testy_celkem: int = int_field(line[1])
        self.potvrzene_pripady_celkem: int = int_field(line[2])
        self.aktivni_pripady: int = int_field(line[3])
        self.vyleceni: int = int_field(line[4])
        self.umrti: int = int_field(line[5])
        self.aktualne_hospitalizovani: int = int_field(line[6])
        self.provedene_testy_vcerejsi_den: int = int_field(line[7])
        self.potvrzene_pripady_vcerejsi_den: int = int_field(line[8])
        self.potvrzene_pripady_dnesni_den: int = int_field(line[9])
        self.provedene_testy_vcerejsi_den_datum: Optional[date] = date_field(line[10])
        self.potvrzene_pripady_vcerejsi_den_datum: Optional[date] = date_field(line[11])
        self.potvrzene_pripady_dnesni_den_datum: Optional[date] = date_field(line[12])
        self.provedene_antigenni_testy_celkem: int = int_field(line[13])
        self.provedene_antigenni_testy_vcerejsi_den: int = int_field(line[14])
        self.provedene_antigenni_testy_vcerejsi_den_datum: Optional[date] = date_field(line[15])
        self.vykazana_ockovani_celkem: int = int_field(line[16])
        self.vykazana_ockovani_vcerejsi_den: int = int_field(line[17])
        self.vykazana_ockovani_vcerejsi_den_datum: Optional[date] = date_field(line[18])
        self.potvrzene_pripady_65_celkem: int = int_field(line[19])
        self.potvrzene_pripady_65_vcerejsi_den: int = int_field(line[20])
        self.potvrzene_pripady_65_vcerejsi_den_datum: Optional[date] = date_field(line[21])
        self.ockovane_osoby_celkem: int = int_field(line[22])
        self.ockovane_osoby_vcerejsi_den: int = int_field(line[23])
        self.ockovane_osoby_vcerejsi_den_datum: Optional[date] = date_field(line[24])


    @staticmethod
    def get(cache_dir: Optional[str]) -> 'ZakladniPrehled' :
        return get_one('zakladni-prehled', ZakladniPrehled, ApiVersion.V2, cache_dir)

