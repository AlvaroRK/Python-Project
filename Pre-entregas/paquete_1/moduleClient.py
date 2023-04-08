class Cliente:
    especie = "humano"

    def __init__(self, nombre, edad, correo, metodoDePago):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.metodoDePago = metodoDePago

    def __str__(self):
        return f"Hola {self.nombre} ingrese los productos que quiera llevar"

    def comprar(self):
        prod = input("Nombre del producto: ")
        cant = int(input("Cantidad del producto: "))
        print(f"{self.nombre} hizo una compra de {cant} {prod} a traves del método de pago: {self.metodoDePago}")

    def cancelarCompra(self):
        print(f"Se canceló correctamente la compra")