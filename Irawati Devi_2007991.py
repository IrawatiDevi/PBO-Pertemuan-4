class Obat:
    def __init__(self, namaobat, dosis, quantity):
        self.namaobat = namaobat
        self.dosis = dosis
        self.quantity = quantity

    def printname(self):
        print(self.namaobat)
        print(self.dosis)
        print(self.quantity)

class tablet(Obat):
     def __init__(self, namaobat, dosis, quantity):
         Obat.__init__(self, namaobat, dosis, quantity)
         self.harga = "Rp. 25.300"

     def tablet(Self):
        print("Nama Obat  : ", Self.namaobat)
        print("Dosis      : ", Self.dosis)
        print("Quantity   : ", Self.quantity)
        print("Harga      : ", Self.harga)


class cair(Obat):
    def __init__(self, namaobat, dosis, quantity):
          Obat.__init__(self, namaobat, dosis, quantity)
          self.harga = "Rp. 16.000"

    def cair(Self):
        print("Nama Obat  : ", Self.namaobat)
        print("Dosis      : ", Self.dosis)
        print("Quantity   : ", Self. quantity)
        print("Harga      : ", Self.harga)

x = tablet("Promag", "Dewasa: 1-2 tablet (3-4 kali sehari)", "1 pack")
y = cair("Mylanta", "Dewasa: 1-2 sendok (3-4 kali sehari)", "50 ml")

x.tablet()
y.cair()