class ItemBase:
    def __init__(self, nombre="", notas=""):
        self.nombre = nombre
        self.notas = notas

    def editar(self, nuevo_nombre=None, nuevas_notas=None):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevas_notas:
            self.notas = nuevas_notas

    def __str__(self):
        return f"{self.nombre} - {self.notas}"