
codigo_producto1="123"
nombre_productos=None

def refrescos():
   DNI=123
   nombre_productos="Coca cola"

def frituras():
    return "Chetos",12.50, "300 gm"
def galletas():
   return "Gansito", 30, "150 gm"

def comprar():
   codigo=input("Anota el codigo del producto: ")
   if codigo_producto1==codigo:
      return refrescos()
   return "Compra1"