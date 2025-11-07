from pint import UnitRegistry
from tkinter import *
from tkinter import ttk
import tempfile
import sys
merne_Kategorije = {
    "Stopa": "ft",
    "Inc": "in",
    "Yard": "yd",
    "Milja": "mi",
    "Nauticka milja": "nmi",
    "Metar": "m",
    "Kilometar": "km",
    'Milimetar': 'mm',
    'Centimetar': 'cm',
    "Unca": "oz",
    "Funta": "lb",
    "Kilogram": "kg",
    "Gram": "gr",
    "Miligram": 'mg',
    "Celzijus": "degC",
    "Farenhajt": "degF",
}

# funkcija koja se poziva dugmetom za izracunavanje

result_label = None


def createLabel():
    global text, result_label
    ureg = UnitRegistry(autoconvert_offset_to_baseunit=True)
    # unit registry da automatski konvertuje jedinice u osnovne
    izMere = mera.get()
    # Skuplja izabranu jedinicu iz comboboxa
    uMeru = mera1.get()
    try:
        # Skuplja drugu izabranu jedninicu iz drugog comboboxa
        kolicinaMere = float(kolicina_value.get())
        # Kolicina jedinice mere za konvert
        a = ureg.parse_units(merne_Kategorije[izMere])
        # poziva se funkcija unit registria za trazenje odgovarajucih mernih jedinica
        b = ureg.parse_units(merne_Kategorije[uMeru])
        # koje su pozvane izborom iz recnika merne_Kategorije
        result = kolicinaMere * a
        # racuna pozvanu jedinicu sa kolicinom
        resultat = result.to(b)
        text = f"{resultat:.2f}"                     # pretvara kolicinu pozvane jedinice u trazenu
    except Exception as x:

        text = str(x)
    if result_label is None:
        result_label = Label(root, text=text, wraplength=300, font='bold')
        result_label.grid(row=9, column=1, pady=20, columnspan=2, sticky='n')
        # Stampa Label sa rezultatom u prozor
    else:
        result_label.config(text=text)


root = Tk()
root.configure(padx=20,pady=20)
if sys.platform.startswith("win"):
    ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
            b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
            b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
            b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

    _, ICON_PATH = tempfile.mkstemp()
    # funkcija za prozor providna ikona i bez teksta "Tk"
    with open(ICON_PATH, 'wb') as icon_file:
        icon_file.write(ICON)
    root.iconbitmap(default=ICON_PATH)
    root.wm_attributes('-transparentcolor')
root.config(borderwidth=10)
root.title('CONVERTER')
root.geometry('400x370')


kolicina_value = StringVar()
mera=StringVar()
mera1=StringVar()
value = list(merne_Kategorije)

kolicina = ttk.Entry(root, textvariable=kolicina_value,font='bold').grid(row=1, column=2, rowspan=2, padx=20, pady=20)
kolicinaLabel = ttk.Label(root, text="Kolicina", anchor="w", font='bold').grid(row=1, column=1, padx=20, pady=20)
mera11 = ttk.Combobox(root, values=value, textvariable=mera, font='bold').grid(row=3, column=2, rowspan=2, padx=20, pady=20)
mera11Label = ttk.Label(root, text="Iz Mere", font='bold').grid(row=3, column=1, padx=20, pady=20)
mera12 = ttk.Combobox(root,values=value, textvariable=mera1, font='bold').grid(row=5, column=2, rowspan=2, padx=20, pady=20)
mera12Label = ttk.Label(root, text="U Meru", font='bold').grid(row=5, column=1, padx=20, pady=20)


button = Button(root, text='Izracunaj', command=createLabel, font='bold')
button.grid(row=7, column=2, sticky="W")
root.mainloop()
if __name__ == "__main__":
    root.mainloop()