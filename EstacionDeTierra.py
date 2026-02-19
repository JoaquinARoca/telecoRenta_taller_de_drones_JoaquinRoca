import tkinter as tk
from dronLink.Dron import Dron

dron = Dron()

ventana = tk.Tk()
ventana.geometry ('750x400')
ventana.title("Pequeña estación de tierra")

# La interfaz tiene 10 filas y una columna

for i in range (10):
    ventana.rowconfigure(i, weight=1)

for i in range (3):
    ventana.columnconfigure(i, weight=1)
# Disponemos ahora los 9 botones
connectBtn = tk.Button(ventana, text="Conectar", bg="dark orange", command = lambda: dron.connect('tcp:127.0.0.1:5763', 115200))
connectBtn.grid(row=0, column=0, padx=3, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

armBtn = tk.Button(ventana, text="Armar", bg="dark orange", command=lambda: dron.arm())
armBtn.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

DespegarTBox = tk.Entry(ventana)
DespegarTBox.grid(row=2,column=1,padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

takeOffBtn = tk.Button(ventana, text="Despegar", bg="dark orange", command=lambda: dron.takeOff(5 if DespegarTBox.get().strip() == "" or int(DespegarTBox.get()) == 0 else int(DespegarTBox.get())))
takeOffBtn.grid(row=2, column=0,  padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

RTLBtn = tk.Button(ventana, text="RTL", bg="dark orange", command=lambda: dron.RTL())
RTLBtn.grid(row=3, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

disconnectBtn = tk.Button(ventana, text="Desconectar", bg="dark orange", command=lambda: dron.disconnect())
disconnectBtn.grid(row=4, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

landBtn = tk.Button(ventana, text="Aterrizar", bg="dark orange", command=lambda: dron.Land())
landBtn.grid(row=5, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

NavegationFrame = tk.LabelFrame(ventana, text="Navegación", bg = "light grey")
NavegationFrame.grid(row=2, column=2, rowspan=4, columnspan=3, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

for i in range(3):
    NavegationFrame.rowconfigure(i,weight=1)
NorthBtn = tk.Button(NavegationFrame, text="No", bg="dark orange", command=lambda: dron.go('North'))
NorthBtn.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

StopBtn = tk.Button(NavegationFrame, text="Stop", bg="dark orange", command=lambda: dron.go('Stop'))
StopBtn.grid(row=1, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)



NWBtn = tk.Button(NavegationFrame, text="NW", bg="dark orange", command=lambda: dron.go('NorthWest'))
NWBtn.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

WestBtn = tk.Button(NavegationFrame, text="We", bg="dark orange", command=lambda: dron.go('West'))
WestBtn.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

SouthWestBtn = tk.Button(NavegationFrame, text="SW", bg="dark orange", command=lambda: dron.go('SouthWest'))
SouthWestBtn.grid(row=2, column=0, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

SouthBtn = tk.Button(NavegationFrame, text="So", bg="dark orange", command=lambda: dron.go('South'))
SouthBtn.grid(row=2, column=1, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

NEBtn = tk.Button(NavegationFrame, text="NE", bg="dark orange", command=lambda: dron.go('NorthEast'))
NEBtn.grid(row=0, column=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

EastBtn = tk.Button(NavegationFrame, text="Ea", bg="dark orange", command=lambda: dron.go('East'))
EastBtn.grid(row=1, column=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)

SEBtn = tk.Button(NavegationFrame, text="SE", bg="dark orange", command=lambda: dron.go('SouthEast'))
SEBtn.grid(row=2, column=2, padx=5, pady=5, sticky=tk.N + tk.S + tk.E + tk.W)


ventana.mainloop()