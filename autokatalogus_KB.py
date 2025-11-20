import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from dataclasses import dataclass
import re
import math

@dataclass
class Auto:
    rendszam: str
    marka: str
    modell: str
    ev: int
    szin: str
    ar: int

class KatalogusKB:
    def __init__(self):
        self.autok = []

    def hozzaad(self, auto: Auto):
        for a in self.autok:
            if a.rendszam.lower() == auto.rendszam.lower():
                raise ValueError("Ez a rendszám már szerepel a listában.")
        self.autok.append(auto)

    def torol(self, rendszam: str):
        uj = [a for a in self.autok if a.rendszam.lower() != rendszam.lower()]
        if len(uj) == len(self.autok):
            raise ValueError("Nincs ilyen rendszám.")
        self.autok = uj

    def modosit(self, eredeti_rendszam: str, uj_auto: Auto):
        for i, a in enumerate(self.autok):
            if a.rendszam.lower() == eredeti_rendszam.lower():
                if uj_auto.rendszam.lower() != eredeti_rendszam.lower():
                    for b in self.autok:
                        if b.rendszam.lower() == uj_auto.rendszam.lower():
                            raise ValueError("Az új rendszám már foglalt.")
                self.autok[i] = uj_auto
                return
        raise ValueError("A módosítandó autó nem található.")

    def lista(self, szuro: str = ""):
        q = szuro.strip().lower()
        if not q:
            return list(self.autok)
        return [a for a in self.autok if q in f"{a.rendszam} {a.marka} {a.modell} {a.szin}".lower()]

def szam_egesz_KB(x, nev):
    try:
        return int(x)
    except:
        raise ValueError(f"{nev} csak egész szám lehet.")

def szam_penz_KB(x, nev):
    try:
        ertek = float(str(x).replace(" ", "").replace(",", ".").replace("Ft", ""))
        return int(math.floor(ertek))
    except:
        raise ValueError(f"{nev} csak szám lehet.")

def penz_formaz_KB(x):
    return f"{x:,} Ft".replace(",", " ")

def rendszam_ellenorzes_KB(rs):
    minta = r"^[A-Z]{3}-\d{3}$"
    if not re.match(minta, rs):
        raise ValueError("Hibás rendszám! Formátum: AAA-111 (3 betű, kötőjel, 3 szám).")

def demo_autok_KB(katalogus: KatalogusKB):
    adatok = [
        Auto("AAA-111", "Toyota", "Corolla", 2018, "fehér", 4490000),
        Auto("BBB-222", "Volkswagen", "Golf", 2020, "szürke", 6290000),
        Auto("CCC-333", "BMW", "320d", 2017, "kék", 6790000),
        Auto("DDD-444", "Suzuki", "Vitara", 2021, "piros", 6890000),
        Auto("EEE-555", "Ford", "Focus", 2016, "fekete", 3290000),
        Auto("FFF-666", "Opel", "Astra", 2019, "ezüst", 3890000),
        Auto("GGG-777", "Kia", "Ceed", 2018, "fehér", 4090000),
        Auto("HHH-888", "Hyundai", "i30", 2020, "szürke", 4590000),
        Auto("III-999", "Honda", "Civic", 2017, "piros", 5190000),
        Auto("JJJ-111", "Mazda", "3", 2021, "kék", 5890000),
        Auto("KKK-222", "Renault", "Megane", 2019, "fehér", 4390000),
        Auto("LLL-333", "Peugeot", "308", 2020, "szürke", 4490000),
        Auto("MMM-444", "Citroen", "C4", 2018, "fekete", 3990000),
        Auto("NNN-555", "Seat", "Leon", 2017, "piros", 4190000),
        Auto("OOO-666", "Skoda", "Octavia", 2021, "fehér", 5690000),
        Auto("PPP-777", "Audi", "A3", 2019, "ezüst", 6490000),
        Auto("QQQ-888", "Mercedes", "A200", 2020, "szürke", 6990000),
        Auto("RRR-999", "Volvo", "V40", 2018, "kék", 6190000),
        Auto("SSS-123", "Nissan", "Qashqai", 2017, "fekete", 5890000),
        Auto("TTT-456", "Tesla", "Model 3", 2022, "fehér", 15500000),
    ]
    for a in adatok:
        try:
            katalogus.hozzaad(a)
        except:
            pass

class AppKB:
    def __init__(self, gyoker):
        self.gyoker = gyoker
        self.gyoker.title("Autókatalógus KB")
        self.katalogus = KatalogusKB()
        self.kivalasztott = None

        fo = ttk.Frame(gyoker, padding=10)
        fo.pack(fill="both", expand=True)

        mezok = ttk.LabelFrame(fo, text="Autó adatai")
        mezok.pack(fill="x")

        self.var_rendszam = tk.StringVar()
        self.var_marka = tk.StringVar()
        self.var_modell = tk.StringVar()
        self.var_ev = tk.StringVar()
        self.var_szin = tk.StringVar()
        self.var_ar = tk.StringVar()

        ttk.Label(mezok, text="Rendszám").grid(row=0, column=0, sticky="w")
        ttk.Entry(mezok, textvariable=self.var_rendszam, width=12).grid(row=1, column=0, padx=4)
        ttk.Label(mezok, text="Márka").grid(row=0, column=1, sticky="w")
        ttk.Entry(mezok, textvariable=self.var_marka, width=12).grid(row=1, column=1, padx=4)
        ttk.Label(mezok, text="Modell").grid(row=0, column=2, sticky="w")
        ttk.Entry(mezok, textvariable=self.var_modell, width=12).grid(row=1, column=2, padx=4)
        ttk.Label(mezok, text="Év").grid(row=0, column=3, sticky="w")
        ttk.Entry(mezok, textvariable=self.var_ev, width=6).grid(row=1, column=3, padx=4)
        ttk.Label(mezok, text="Szín").grid(row=0, column=4, sticky="w")
        ttk.Entry(mezok, textvariable=self.var_szin, width=10).grid(row=1, column=4, padx=4)
        ttk.Label(mezok, text="Ár").grid(row=0, column=5, sticky="w")
        ttk.Entry(mezok, textvariable=self.var_ar, width=10).grid(row=1, column=5, padx=4)

        gombok = ttk.Frame(fo)
        gombok.pack(fill="x", pady=5)
        ttk.Button(gombok, text="Hozzáadás", command=self.hozzaad).pack(side="left", padx=4)
        ttk.Button(gombok, text="Módosítás", command=self.modosit).pack(side="left", padx=4)
        ttk.Button(gombok, text="Törlés", command=self.torol).pack(side="left", padx=4)
        ttk.Button(gombok, text="TXT mentés", command=self.mentes_txt).pack(side="left", padx=4)
        ttk.Button(gombok, text="Kilépés", command=self.kilepes).pack(side="right", padx=4)

        szuro = ttk.Frame(fo)
        szuro.pack(fill="x")
        ttk.Label(szuro, text="Keresés:").pack(side="left")
        self.var_keres = tk.StringVar()
        ttk.Entry(szuro, textvariable=self.var_keres, width=25).pack(side="left", padx=5)
        self.var_keres.trace_add("write", lambda *a: self.frissit())

        lista_kont = ttk.Frame(fo)
        lista_kont.pack(fill="both", expand=True, pady=5)
        self.lista = tk.Listbox(lista_kont, height=12)
        self.lista.pack(side="left", fill="both", expand=True)
        g = ttk.Scrollbar(lista_kont, command=self.lista.yview)
        g.pack(side="right", fill="y")
        self.lista.config(yscrollcommand=g.set)
        self.lista.bind("<<ListboxSelect>>", self.kijeloles)

        self.statusz = tk.StringVar(value="Készenlét")
        ttk.Label(fo, textvariable=self.statusz, anchor="w").pack(fill="x", pady=(4,0))

        demo_autok_KB(self.katalogus)
        self.frissit()

    def sor(self, a: Auto):
        return f"{a.rendszam} | {a.marka} {a.modell} | {a.ev} | {a.szin} | {penz_formaz_KB(a.ar)}"

    def frissit(self):
        self.lista.delete(0, tk.END)
        for a in self.katalogus.lista(self.var_keres.get()):
            self.lista.insert(tk.END, self.sor(a))
        self.statusz.set(f"Találatok: {self.lista.size()}")

    def kijeloles(self, e=None):
        i = self.lista.curselection()
        if not i:
            return
        sor = self.lista.get(i[0])
        rs = sor.split("|")[0].strip()
        self.kivalasztott = rs
        for a in self.katalogus.autok:
            if a.rendszam == rs:
                self.var_rendszam.set(a.rendszam)
                self.var_marka.set(a.marka)
                self.var_modell.set(a.modell)
                self.var_ev.set(str(a.ev))
                self.var_szin.set(a.szin)
                self.var_ar.set(str(a.ar))
                break

    def beolvas(self):
        r = self.var_rendszam.get().strip().upper()
        rendszam_ellenorzes_KB(r)
        m = self.var_marka.get().strip()
        mo = self.var_modell.get().strip()
        e = szam_egesz_KB(self.var_ev.get(), "Év")
        s = self.var_szin.get().strip() or "ismeretlen"
        a = szam_penz_KB(self.var_ar.get(), "Ár")
        if not r or not m or not mo:
            raise ValueError("Hiányzó adat.")
        return Auto(r, m, mo, e, s, a)

    def hozzaad(self):
        try:
            a = self.beolvas()
            self.katalogus.hozzaad(a)
            self.frissit()
            self.statusz.set("Hozzáadva.")
        except Exception as ex:
            messagebox.showerror("Hiba", str(ex))

    def modosit(self):
        if not self.kivalasztott:
            messagebox.showinfo("Figyelem", "Nincs kijelölt elem.")
            return
        try:
            uj = self.beolvas()
            self.katalogus.modosit(self.kivalasztott, uj)
            self.frissit()
            self.statusz.set("Módosítva.")
            self.kivalasztott = uj.rendszam
        except Exception as ex:
            messagebox.showerror("Hiba", str(ex))

    def torol(self):
        if not self.kivalasztott:
            messagebox.showinfo("Figyelem", "Nincs kijelölt elem.")
            return
        if messagebox.askyesno("Törlés", f"Törlöd: {self.kivalasztott}?"):
            try:
                self.katalogus.torol(self.kivalasztott)
                self.kivalasztott = None
                self.frissit()
                self.statusz.set("Törölve.")
            except Exception as ex:
                messagebox.showerror("Hiba", str(ex))

    def mentes_txt(self):
        utvonal = filedialog.asksaveasfilename(
            title="Mentés TXT fájlba",
            defaultextension=".txt",
            filetypes=[("Szövegfájl", "*.txt"), ("Minden fájl", "*.*")]
        )
        if not utvonal:
            return
        try:
            with open(utvonal, "w", encoding="utf-8") as f:
                for a in self.katalogus.lista(self.var_keres.get()):
                    f.write(self.sor(a) + "\n")
            self.statusz.set(f"Elmentve: {utvonal}")
        except Exception as ex:
            messagebox.showerror("Hiba", str(ex))

    def kilepes(self):
        self.gyoker.destroy()